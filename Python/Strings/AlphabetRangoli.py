import string

def print_rangoli(size):
    pattern_list = [[string.ascii_lowercase[size - 1]]]
    current_size = size - 1

    while current_size > 0:
        row = []

        for i in range(size, current_size - 1, -1):
            row.append(string.ascii_lowercase[i - 1])

        row += list(reversed(row))[1:]
        pattern_list.append(row)
        current_size -= 1

    padding = len(pattern_list[-1]) * 2 - 1

    for i in range(len(pattern_list)):
        print("-".join(pattern_list[i]).center(padding, "-"))

    for i in range(len(pattern_list) - 2, -1, -1):
        print("-".join(pattern_list[i]).center(padding, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)