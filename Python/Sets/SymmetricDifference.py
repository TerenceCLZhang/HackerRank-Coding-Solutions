# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
M_set = set(map(int, input().split()))
N = int(input())
N_set = set(map(int, input().split()))

diff = sorted(M_set.symmetric_difference(N_set))

for num in diff:
    print(num)