def print_formatted(number):
    padding = len(bin(number)[2:])
    for num in range(1, number + 1):
        print(f"{str(num).rjust(padding, ' ')} {str(oct(num))[2:].rjust(padding, ' ')} {str(hex(num))[2:].upper().rjust(padding, ' ')} {str(bin(num))[2:].rjust(padding, ' ')}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)