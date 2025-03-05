from math import sqrt

for _ in range(int(input())):
    n = int(input())
    
    if n <= 1:
        print("Not prime")
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")