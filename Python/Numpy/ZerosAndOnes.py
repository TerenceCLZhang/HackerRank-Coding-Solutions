import numpy as np

sizes = tuple(map(int, input().split()))
print(np.zeros(sizes, dtype = int))
print(np.ones(sizes, dtype = int))