from marko.ext.latex_renderer import LatexRenderer
from marko import (inline, block)
import re

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
        
class Author(BlockElementWithPattern):
    pattern = re.compile(r'Author: (.*)')
    
class Preface(BlockElementWithPattern):
    pattern = re.compile(r'Preface:\s(.*)')
    parse_children = True

class MarkoLatexRenderer(LatexRenderer):
    author = ''
    preface = ''
    def render_document(self, element):
        # should come first to collect needed packages
        children = self.render_children(element)
        # create document parts
        # items = ["\\documentclass{article}"]
        # add used packages
        # items.extend(f"\\usepackagep" for p in self._packages)
        # add inner content
        # items.append(self._environment("document", children))
        return self._environment2("article", children, [self.article_name, self.author])
    
    def render_author(self, element):
        self.author = element.content
        return ''
    
    def render_preface(self, element):
        self.preface = element.content
        print('got preface', self.preface)
        return ''
    
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
            _logger.warning("Setting a title for links is not supported!")
        body = self.render_children(element)
        return f"\\href{{{element.dest}}}{{{body}}} \\footnote{{{self._escape_latex(element.dest)}}}"
    
    def render_list(self, element):
        children = self.render_children(element)
        env = "enumerate" if element.ordered else "itemize"
        # TODO: check how to handle element.start with ordered list
        if element.start and element.start != 1:
            _logger.warning("Setting the starting number of the list is not supported!")
        return self._environment(env, children, ['leftmargin=0.5cm'])
            
    def render_image(self, element):
        return f"""
            % \\end{{multicols}}
            \\begin{{center}}
                \\includegraphics[width=\\linewidth]{{{element.dest}}}
            \\end{{center}}
            % \\begin{{multicols}}{{2}}
        """
    
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
    elements=[BlockMath, BlockMathInParagraph, InlineMath, Author]
    renderer_mixins = [MarkoLatexRenderer]

def make_extension(*args):
    return MarkoLatexExtension(*args)
