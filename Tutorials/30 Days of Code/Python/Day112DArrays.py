#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = -float("inf")
    
    for i in range(4):
        for j in range(4):
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +  # Top row
                arr[i+1][j+1] +  # Middle element
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]  # Bottom row
            )
            max_sum = max(max_sum, current_sum)
    
    print(max_sum)
        