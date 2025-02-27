# Enter your code here. Read input from STDIN. Print output to STDOUT

countries = set()

N = int(input())

for _ in range(N):
    countries.add(input())

print(len(countries))