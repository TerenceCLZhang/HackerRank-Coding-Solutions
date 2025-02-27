# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = input().split()
    other_set = set(map(int, input().split()))
    if command[0] == "intersection_update":
        A.intersection_update(other_set)
    if command[0] == "update":
        A.update(other_set)
    if command[0] == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)
    if command[0] == "difference_update":
        A.difference_update(other_set)
    
print(sum(A))