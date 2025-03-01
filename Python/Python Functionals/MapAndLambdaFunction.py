cube = lambda x: x ** 3

def fibonacci(n):
    # return a list of fibonacci numbers
    ans = []

    if n <= 0:
        return ans

    f1, f2 = 0, 1
    ans.append(f1)

    for i in range(1, n):
        ans.append(f2)
        f1, f2 = f2, f1 + f2
        
    return ans

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))