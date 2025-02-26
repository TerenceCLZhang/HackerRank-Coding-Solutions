if __name__ == '__main__':
    array = []
    N = int(input())
    for _ in range(N):
        command = input()
        num = len(command.split())

        if num == 1:
            if command == "print":
                print(array)
            if command == "sort":
                array.sort()
            if command == "reverse":
                array.reverse()
            if command == "pop":
                array.pop()

        if num == 2:
            first, second = command.split()
            second = int(second)
            if first == "remove":
                array.remove(second)
            if first == "append":
                array.append(second)

        if num == 3:
            first, second, third = command.split()
            second, third = int(second), int(third)
            if first == "insert":
                array.insert(second, third)