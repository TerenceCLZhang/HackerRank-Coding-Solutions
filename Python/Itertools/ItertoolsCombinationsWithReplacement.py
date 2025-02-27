# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S, k = input().split()
for comb in sorted(list(sorted(x) for x in combinations_with_replacement(S, int(k)))):
    print("".join(comb))