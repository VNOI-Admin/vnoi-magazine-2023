from sys import stdin, stderr
import yaml
import re

stdin.reconfigure(encoding="utf-8-sig")

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

lines = list(s.strip() for s in stdin)
content = '\n'.join(lines)
match = re.match(r'---\n([\s\S]*?)\n---\n([\s\S]*)', content, re.M)

if match is None:
    front_matter = '{}'
    interview_content = content
else:
    front_matter = match.group(1)
    interview_content = match.group(2)
    
front_matter_data = yaml.safe_load(front_matter)
Q = front_matter_data.get('Q', 'Q')
A = front_matter_data.get('A', 'A')

print(f'\\def\\Qtext{{{Q}}}')
print(f'\\def\\Atext{{{A}}}')

for line in interview_content.split('\n'):
    line = line.strip()
    if line == '':
        continue
    line = escape_latex(line)
    line = re.sub('^Q:', r'\\interviewQ', line)
    line = re.sub('^A:', r'\\interviewA', line)
    print(line)
    print()
