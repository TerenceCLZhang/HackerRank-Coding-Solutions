# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
Student = namedtuple("Student", input().split())

print(sum(int(Student(*input().split()).MARKS) for _ in range(N)) / N)