# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    uid_to_check = input()
    if re.match(r"^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}$", uid_to_check):
        print("Valid")
    else:
        print("Invalid")