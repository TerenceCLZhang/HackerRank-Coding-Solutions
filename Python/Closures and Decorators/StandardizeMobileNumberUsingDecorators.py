def wrapper(f):
    def fun(l):
        l = [f"+91 {x[-10:-5]} {x[-5:]}" for x in l]
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 