import numpy as np

N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.transpose(arr))
print(arr.flatten())