#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    capatilized_string = ""
    for i, char in enumerate(s):
        if i == 0 or not char.isupper() and s[i - 1] == " ":
            capatilized_string += char.upper()
        else:
            capatilized_string += char
    return capatilized_string
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
