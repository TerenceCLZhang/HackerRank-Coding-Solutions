# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
english_letters = input().split()
K = int(input())

combs = list(combinations(english_letters, K))

count = 0
for comb in combs:
    if "a" in comb:
        count += 1

print(count / len(combs))