import numpy as np

N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])
arr_sum = np.sum(arr, axis=0)
print(np.prod(arr_sum))