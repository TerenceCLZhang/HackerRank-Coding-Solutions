# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
shoe_sizes = Counter(list(map(int, input().split())))
N = int(input())

total_price = 0
for _ in range(N):
    shoe_size, price = map(int, input().split())
    if shoe_size in shoe_sizes and shoe_sizes[shoe_size] > 0:
        total_price += price
        shoe_sizes[shoe_size] -= 1

print(total_price)