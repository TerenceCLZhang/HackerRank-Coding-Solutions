# Naive Approach

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    arr.sort()
    
    for i in range(n - 2, -1, -1):
        if sorted_arr[i] != sorted_arr[-1]:
            print(sorted_arr[i])
            break


# Two Pass Search Approach

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    largest = -101
    second_largest = -101
    
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    
    for i in range(n):
        if arr[i] > second_largest and largest != arr[i]:
            second_largest = arr[i]
    
    print(second_largest)


# One Pass Search Approach

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    largest = -101
    second_largest = -101
    
    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] < largest:
            second_largest = arr[i]
    
    print(second_largest)
