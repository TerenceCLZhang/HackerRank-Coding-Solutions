# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    queue = deque(arr)
    last_picked = float('inf')
    
    while queue:
        pick = queue.popleft() if queue[0] >= queue[-1] else queue.pop()
        
        if pick > last_picked:
            print("No")
            break
        
        last_picked = pick
    else:
        print("Yes")