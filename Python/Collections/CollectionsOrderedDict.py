# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

item_price = OrderedDict()

for _ in range(int(input())):
    item, price = input().rsplit(" ", 1)
    if item in item_price:
        item_price[item] += int(price)
    else:
        item_price[item] = int(price)

for item, price in item_price.items():
    print(item, price)