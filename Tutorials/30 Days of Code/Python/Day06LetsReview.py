for _ in range(int(input())):
    s = input()

    even = ""
    odd = ""

    for i, char in enumerate(s):
        if i % 2 == 0:
            even += char
        else:
            odd += char
    
    print(f"{even} {odd}")