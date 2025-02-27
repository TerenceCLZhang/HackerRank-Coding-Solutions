# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")