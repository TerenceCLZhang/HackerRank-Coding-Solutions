# Non Regular Expression Approach

for _ in range(int(input())):
    n = input()
    if "." not in n:
        print(False)
    else:
        try:
            n_float = float(n)
            print(True)
        except:
            print(False)


# Regular Expression Approach

import re

for _ in range(int(input())):
    print(bool(re.fullmatch(r"^[+\-]?\d*\.\d+$", input())))