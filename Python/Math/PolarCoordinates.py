# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import polar

z = complex(input())
r, theta = polar(z)
print(r)
print(theta)