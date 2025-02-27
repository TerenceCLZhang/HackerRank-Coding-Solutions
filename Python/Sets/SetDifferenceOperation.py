# Enter your code here. Read input from STDIN. Print output to STDOUT

english = int(input())
english_set = set(map(int, input().split()))
french = int(input())
french_set = set(map(int, input().split()))

difference_set = english_set.difference(french_set)
print(len(difference_set))
