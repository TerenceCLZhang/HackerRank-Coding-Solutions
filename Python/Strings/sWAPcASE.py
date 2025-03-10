# Using swapcase()

def swap_case(s):
    result = ""
    for letter in s:
        result += letter.swapcase()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


## Without using swapcase()

def swap_case(s):
    result = ""
    for letter in s:
        if letter.isupper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

    