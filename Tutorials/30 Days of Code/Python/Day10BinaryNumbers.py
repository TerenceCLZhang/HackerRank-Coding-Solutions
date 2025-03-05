#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    bin_string = bin(n)[2:]
    
    largest = 0
    current_largest = 0
    
    for d in bin_string:
        if d == '1':
            current_largest += 1
        else:
            largest = max(largest, current_largest)
            current_largest = 0
    
    largest = max(largest, current_largest) # Last Check
    
    print(largest)