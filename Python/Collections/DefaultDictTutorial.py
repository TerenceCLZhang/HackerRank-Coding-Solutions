# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)

for i in range(n):
    A[input()].append(i + 1)
    
for i in range(m):
    b = input()
    print(*A[b] if b in A else [-1])