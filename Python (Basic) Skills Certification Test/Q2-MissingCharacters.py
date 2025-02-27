#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    numbers = set("0123456789")
    characters = set("abcdefghijklmnopqrstuvwxyz")
    
    s_set = set(s)
    
    missing_numbers = sorted(numbers - s_set)
    missing_characters = sorted(characters - s_set)
    
    return "".join(missing_numbers + missing_characters)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
