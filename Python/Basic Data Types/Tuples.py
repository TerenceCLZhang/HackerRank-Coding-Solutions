# Note: This problem is only solvable on Python 2 as Python 3 gives a different hash value

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))
