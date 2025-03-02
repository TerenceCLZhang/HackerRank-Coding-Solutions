#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_format = "%d %b %Y %H:%M:%S %z"
    
    t1 = dt.strptime(" ".join(t1.split()[1:]), date_format)
    t2 = dt.strptime(" ".join(t2.split()[1:]), date_format)
    
    return str(abs(int((t1 - t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
