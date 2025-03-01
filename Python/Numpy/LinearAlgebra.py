import numpy as np

N = int(input())
A = np.array([list(map(float, input().split())) for _ in range(N)])
print(round(np.linalg.det(A), 2))