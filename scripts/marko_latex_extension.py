from marko.ext.latex_renderer import LatexRenderer
from marko import (inline, block)
import re
import yaml

class BlockElementWithPattern(block.BlockElement):
    priority=100
    pattern=None
    include_children=False
   
    def __init__(self, match):
        self.content = match.group(1)

    @classmethod
    def match(cls, source):
        return source.expect_re(cls.pattern)

    @classmethod
    def parse(cls, source):
        m = source.match
        source.consume()
        return m

class BlockMathInParagraph(inline.InlineElement):
    priority=101
    pattern = r'\$\$([\s\S]*?)\$\$'
    parse_children = False
   
    def __init__(self, match):
        self.content = match.group(1)
    
class InlineMath(inline.InlineElement):
    priority=100
    pattern = r'\$([\s\S]*?)\$'
    parse_children = False
    
    def __init__(self, match):
        self.content = match.group(1)
        
class BlockMath(BlockElementWithPattern):
    pattern=re.compile(r'\$\$([\s\S]*?)\$\$', flags=re.M)
    
class FrontMatter(BlockElementWithPattern):
    pattern = re.compile(r'---\n(.*?)\n---', re.M | re.DOTALL)
    def __init__(self, match):
        super().__init__(match)
        self.data = yaml.safe_load(self.content)

class LatexTabular(BlockElementWithPattern):
    pattern = re.compile(r'(\\begin\{tabular\}[\s\S]*\\end\{tabular\})', re.M)
    
class LatexTabularx(BlockElementWithPattern):
    pattern = re.compile(r'(\\begin\{tabularx\}[\s\S]*\\end\{tabularx\})', re.M)
    
class LatexLongTable(BlockElementWithPattern):
    pattern = re.compile(r'(\\begin\{longtable\}[\s\S]*\\end\{longtable\})', re.M)
    
class LatexMinipage(BlockElementWithPattern):
    pattern = re.compile(r'(\\begin\{minipage\}[\s\S]*\\end\{minipage\})', re.M)
    
class Preface(BlockElementWithPattern):
    pattern = re.compile(r'Preface:\s(.*)')
    parse_children = True
    
class CustomFootnote(inline.InlineElement):
    pattern=r'\[\{(.*)\}\]'
    parse_children = False
    
    def __init__(self, match):
        self.content = match.group(1)
        
class Strikethrough(inline.InlineElement):
    pattern=r'\~\~(.*)\~\~'
    parse_children = False
    
    def __init__(self, match):
        self.content = match.group(1)
        
class Emoji(inline.InlineElement):
    pattern=r'\:(.*)\:'
    parse_children = False
    
    def __init__(self, match):
        self.emoji_name = match.group(1)

class MarkoLatexRenderer(LatexRenderer):
    front_matter = {}
    
    def render_document(self, element):
        children = self.render_children(element)
        def get(field):
            return self.front_matter.get(field, '')
        return self._environment2("article", children, [
            get('title'),
            get('subtitle'),
            get('author')
        ])
    
    def render_heading(self, element):
        children = self.render_children(element)
        if element.level == 1:
            self.article_name = children
            return ""
        return super().render_heading(element)
    
    def render_fenced_code(self, element):
        language = self._escape_latex(element.lang).strip().lower()
        if 'c++' in language or 'cpp' in language:
            language = 'cpp'
        if 'py' in language or 'python' in language:
            language = 'python'
        if language not in ['c', 'cpp', 'python', 'text']:
            language = 'text'
        return self._environment(f"{language}code", element.children[0].children)
    
    def render_block_math(self, element):
        # print('block math', element.content)
        return f"$${element.content}$$"
    
    def render_block_math_in_paragraph(self, element):
        # print('block math in paragraph', element.content)
        return f"$${element.content}$$"
    
    def render_inline_math(self, element):
        # print('inline math', element.content)
        return f"${element.content}$"
    
    def render_link(self, element):
        if element.title:
            print("Setting a title for links is not supported!")
        body = self.render_children(element)
        # return f"\\href{{{element.dest}}}{{{body}}} \\footnote{{{self._escape_latex(element.dest)}}}"
        return f"\\insertLink{{ {self._escape_latex(element.dest)} }}{{ {body} }}"
    
    def render_list(self, element):
        children = self.render_children(element)
        env = "enumerate" if element.ordered else "itemize"
        # TODO: check how to handle element.start with ordered list
        if element.start and element.start != 1:
            print("Setting the starting number of the list is not supported!")
        return self._environment(env, children, ['leftmargin=0.5cm'])
            
    def render_image(self, element):
        children = self.render_children(element)
        
        return f"\\includeImage{{ {element.dest} }}{{ {children} }}"
        
    def render_custom_footnote(self, element):
        return f"\\footnote{{ {element.content} }}"
    
    def render_strikethrough(self, element):
        return f"\\sout{{ {element.content} }}"
    
    def render_html_block(self, element):
        print("Rendering HTML is not supported!")
        print(element.children)
        return ""
    
    def render_latex_tabular(self, element):
        return r'\begin{center}' + element.content + r'\end{center}'
    
    def render_latex_tabularx(self, element):
        return r'\begin{center}' + element.content + r'\end{center}'
    
    def render_latex_long_table(self, element):
        return r'\begin{center}' + element.content + r'\end{center}'
    
    def render_latex_minipage(self, element):
        return r'\begin{center}' + element.content + r'\end{center}'
    
    def render_emoji(self, element):
        return f'\\{element.emoji_name}'
    
    def render_line_break(self, element):
        # always soft
        return '\n'
    
    def render_front_matter(self, element):
        self.front_matter = element.data
        return ''
    
    @staticmethod
    def _escape_latex(text: str) -> str:
        # print('escaping', text)
        # Special LaTeX Character:  # $ % ^ & _ { } ~ \
        specials = {
            "#": "\\#",
            "$": "\\$",
            "%": "\\%",
            "&": "\\&",
            "_": "\\_",
            "{": "\\{",
            "}": "\\}",
            "^": "\\^{}",
            "~": "\\~{}",
            "\\": "\\textbackslash{}",
        }

        return "".join(specials.get(s, s) for s in text)
    
    @staticmethod
    def _environment2(env_name: str, content: str, options = ()):
        options_str = f"{''.join(map(lambda s: '{' + s + '}', options))}" if options else ""
        return f"\\begin{{{env_name}}}{options_str}\n{content}\\end{{{env_name}}}\n"
    
class MarkoLatexExtension:
    elements=[
            BlockMath,
            BlockMathInParagraph,
            InlineMath,
            CustomFootnote,
            Strikethrough,
            LatexTabular,
            LatexLongTable,
            LatexMinipage,
            LatexTabularx,
            Emoji,
            FrontMatter
        ]
    renderer_mixins = [MarkoLatexRenderer]

def make_extension(*args):
    return MarkoLatexExtension(*args)
