# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = float(input())
BC = float(input())

angle = math.degrees(math.atan2(AB, BC))

print(f"{round(angle)}{chr(176)}")