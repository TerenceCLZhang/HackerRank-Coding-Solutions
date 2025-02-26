# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def convert(match):
    symbol = match.group(0)
    return "or" if "||" in symbol else "and"

N = int(input())
for _ in range(N):
    print(re.sub(r"(?<=\s)(&{2}|[|]{2})(?=\s)", convert, input()))
