# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for _ in range(int(input())):
    instruction = input().split()
    if instruction[0] == "pop":
        d.pop()
    if instruction[0] == "popleft":
        d.popleft()
    if instruction[0] == "append":
        d.append(instruction[1])
    if instruction[0] == "appendleft":
        d.appendleft(instruction[1])

print(*d)