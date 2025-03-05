#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    total_num_swaps = 0
    
    for i in range(len(a)):
        num_swaps = 0#!/bin/python3

import math
import os
import random
import re
import sys

def bubble_sort(a):
    total_num_swaps = 0

    for i in range(len(a)):
        num_swaps = 0
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1
        
        if num_swaps == 0:
            break
            
        total_num_swaps += num_swaps
        
    return total_num_swaps

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    total_num_swaps = bubble_sort(a)
    
    print(f"Array is sorted in {total_num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1
        
        if num_swaps == 0:
            break
            
        total_num_swaps += num_swaps
        
    print(f"Array is sorted in {total_num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
