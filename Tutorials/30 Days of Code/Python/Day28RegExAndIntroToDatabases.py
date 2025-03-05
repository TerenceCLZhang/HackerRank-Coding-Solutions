#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())
    
    email_database = {}

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if emailID not in email_database and re.match(r"^[a-z]{1,20}$", firstName) and re.match(r"^[a-z@.]{1,50}@gmail.com$", emailID):
            email_database[emailID] = firstName
    
    sorted_database = sorted(email_database.items(), key=lambda x: x[1])

    for _, name in sorted_database:
        print(name)
    