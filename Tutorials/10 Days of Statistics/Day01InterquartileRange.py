#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    arr = []
    
    for v, f in zip(values, freqs):
        arr.extend([v] * f)
        
    q1, _, q3 = quartiles(arr)
    iqr = q3 - q1
    
    print(f"{iqr:.1f}")

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
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
