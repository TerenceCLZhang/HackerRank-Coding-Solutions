import numpy as np

N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])
arr_min = np.min(arr, axis=1)
print(np.max(arr_min))