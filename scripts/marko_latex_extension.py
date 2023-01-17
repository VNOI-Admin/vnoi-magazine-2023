from marko.ext.latex_renderer import LatexRenderer
from marko import (inline, block)
import re

class BlockMath(block.BlockElement):
    priority=3
    pattern=re.compile(r'\$\$([\s\S]*?)\$\$', flags=re.M)
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
    
class InlineMath(inline.InlineElement):
    priority=3
    pattern = r'\$([\s\S]*?)\$'
    parse_children = True
    
    def __init__(self, match):
        self.content = match.group(1)
    

class MarkoLatexRenderer(LatexRenderer):
    def render_document(self, element):
        # should come first to collect needed packages
        children = self.render_children(element)
        # create document parts
        # items = ["\\documentclass{article}"]
        # add used packages
        # items.extend(f"\\usepackage{{{p}}}" for p in self._packages)
        # add inner content
        # items.append(self._environment("document", children))
        return children
    
    def render_fenced_code(self, element):
        language = self._escape_latex(element.lang).strip().lower()
        if language == 'c++':
            language = 'cpp'
        if language not in ['c', 'cpp', 'python', 'text']:
            language = 'text'
        return self._environment(f"{language}code", element.children[0].children)
    
    def render_block_math(self, element):
        return f"$${element.content}$$"
    
    def render_inline_math(self, element):
        return f"${element.content}$"
    
class MarkoLatexExtension:
    elements=[BlockMath, InlineMath]
    renderer_mixins = [MarkoLatexRenderer]

def make_extension(*args):
    return MarkoLatexExtension(*args)