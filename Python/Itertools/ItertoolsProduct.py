# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(*product(A, B))