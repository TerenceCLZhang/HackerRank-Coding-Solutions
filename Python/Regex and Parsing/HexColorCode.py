# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

css_text = "\n".join([input() for _ in range(int(input()))])

blocks = re.findall(r'\{([^}]*)\}', css_text)

for block in blocks:
    colors = re.findall(r"#[A-Fa-f0-9]{3,6}\b", block)
    for color in colors:
        print(color)