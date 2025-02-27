# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = tuple(input().split())

arr = list(input().split())

A = set(input().split())
B = set(input().split())

happiness = (sum(1 if num in A else -1 if num in B else 0 for num in arr))
print(happiness)