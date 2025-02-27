# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input().split())
n = int(input())

for _ in range(n):
    other_set = set(input().split())
    if not A.issuperset(other_set):
        print(False)
        break
else:
    print(True)