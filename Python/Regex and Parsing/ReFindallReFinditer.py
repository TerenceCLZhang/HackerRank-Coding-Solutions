# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

matches = re.findall(r'(?i)(?<=[b-df-hj-np-tv-z])([aeiou]{2,})(?=[b-df-hj-np-tv-z])', input())

if matches:
    for m in matches:
        print(m)
else:
    print(-1)