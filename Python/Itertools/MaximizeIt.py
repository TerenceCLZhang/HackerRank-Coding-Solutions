# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

def function(nums, M):
    return sum(num ** 2 for num in nums) % M


K, M = tuple(map(int, input().split()))
lists = [list(map(int, input().split()))[1:] for _ in range(K)]

combs = product(*lists)
max_val = max(function(comb, M) for comb in combs)
print(max_val)