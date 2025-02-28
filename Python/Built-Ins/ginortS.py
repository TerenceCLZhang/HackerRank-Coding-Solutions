# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()

lower = sorted([char for char in S if char.islower()])
upper = sorted([char for char in S if char.isupper()])
odd = sorted([char for char in S if char.isdigit() and int(char) % 2 == 1])
even = sorted([char for char in S if char.isdigit() and int(char) % 2 == 0])

print("".join(lower + upper + odd + even))