#!/bin/python3

import math
import os
import random
import re
import sys


# NOTE: Need to delete "if __name__ = "__main__":" for the code to work

S = input()

try:
    i = int(S)
    print(i)
except ValueError:
    print("Bad String")