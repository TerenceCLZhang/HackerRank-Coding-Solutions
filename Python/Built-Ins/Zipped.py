# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split())
grades = [map(float, input().split()) for _ in range(X)]

grades = zip(*grades)

for subject in grades:
    print(sum(subject) / X)
