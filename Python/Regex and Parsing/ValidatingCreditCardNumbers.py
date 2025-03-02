# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    card_number = input()

    if not re.match(r"^(4|5|6)\d{3}(-?\d{4}){3}$", card_number):
        print("Invalid")
    else:
        sanitized_card_number = card_number.replace("-", "")

        if re.search(r"(\d)\1{3,}", sanitized_card_number):
            print("Invalid")
        else:
            print("Valid")