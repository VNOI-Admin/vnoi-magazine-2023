from sys import stdin

def escape_latex(text: str) -> str:
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

for line in stdin.readlines():
    print(escape_latex(line))
