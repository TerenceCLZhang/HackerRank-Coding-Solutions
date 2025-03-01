import numpy as np

def arrays(arr):
    return np.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)