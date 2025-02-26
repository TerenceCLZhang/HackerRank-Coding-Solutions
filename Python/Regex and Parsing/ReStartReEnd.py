# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
k = input()

matches = list(re.finditer(f'(?=({k}))', s))

if matches:
    for m in matches:
        print((m.start(1), m.end(1) - 1))
else:
    print((-1, -1))