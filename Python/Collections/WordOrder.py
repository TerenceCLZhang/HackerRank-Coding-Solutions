# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

repeated = Counter(input() for _ in range(int(input())))

print(len(repeated))
print(*repeated.values())