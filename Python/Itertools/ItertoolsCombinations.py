# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = input().split()
for i in range(1, int(k) + 1):
    for comb in sorted(list(sorted(x) for x in combinations(S, i))):
        print("".join(comb))