#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    n = len(arr)
    mean = sum(arr) / n
    variance = sum((num - mean) ** 2 for num in arr) / n
    std_dev = math.sqrt(variance)
    print(f"{std_dev:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
