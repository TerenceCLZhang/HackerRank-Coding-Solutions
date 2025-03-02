#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Transpose the matrix to read columns top-to-bottom
decoded_string = ''.join([''.join(col) for col in zip(*matrix)])

# Use regex to replace symbols/spaces between alphanumeric characters with a space
output = re.sub(r'(?<=\w)[^a-zA-Z0-9]+(?=\w)', ' ', decoded_string)

print(output)