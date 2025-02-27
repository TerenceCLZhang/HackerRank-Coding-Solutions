# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
room_number_list = list(input().split())

seen = set()
duplicates = set()

for room in room_number_list:
    if room in seen:
        duplicates.add(room)
    else:
        seen.add(room)

captains_room = seen.difference(duplicates).pop()
print(captains_room)