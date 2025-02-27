# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()
perms = list(permutations(S, int(k)))
for perm in sorted(perms):
    print("".join(perm))