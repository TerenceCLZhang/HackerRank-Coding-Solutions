#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    arr.sort()
    
    q2 = get_median(arr)
    
    lower_half = arr[:len(arr) // 2]
    upper_half = arr[(len(arr) + 1) // 2:]
    
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    
    return [q1, q2, q3]

def get_median(arr):
    middle_index = len(arr) // 2
    median = arr[middle_index] if len(arr) % 2 == 1 else (arr[middle_index - 1] + arr[middle_index]) / 2
    return int(median)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
