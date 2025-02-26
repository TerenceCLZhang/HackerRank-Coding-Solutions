# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = tuple(map(int, input().split()))

pattern = ".|."
dup_pattern = 1

for row in range(N):
    if row < N // 2:
        row_pattern = pattern * dup_pattern
        print(row_pattern.center(M, "-"))
        dup_pattern += 2
        
    if row == N // 2:
        print("WELCOME".center(M, "-"))

    if row > N // 2:
        dup_pattern -= 2
        row_pattern = pattern * dup_pattern
        print(row_pattern.center(M, "-"))