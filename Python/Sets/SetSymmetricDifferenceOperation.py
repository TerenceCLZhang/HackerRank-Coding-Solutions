# Enter your code here. Read input from STDIN. Print output to STDOUT

english = int(input())
english_set = set(map(int, input().split()))
french = int(input())
french_set = set(map(int, input().split()))

symmetric_difference_set = english_set.symmetric_difference(french_set)
print(len(symmetric_difference_set))
