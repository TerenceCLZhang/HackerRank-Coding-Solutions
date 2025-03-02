#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    
    char_count = Counter(s)
    char_count = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    for k, v in char_count[:3]:
        print(k, v)