# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

result = []
S = input()
for group in groupby(S):
    num, val = list(group)
    result.append((sum(1 for _ in val), int(num)))
print(*result)