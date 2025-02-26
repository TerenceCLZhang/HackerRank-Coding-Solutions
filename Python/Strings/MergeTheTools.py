def remove_duplicates(string):
    result = []
    seen = set()
    for char in string:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return "".join(result)

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i: i + k]
        print(remove_duplicates(substring))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)