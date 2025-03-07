def get_mean(arr):
    mean = sum(arr) / len(arr)
    return mean

def get_median(arr):
    middle_index = len(arr) // 2
    median = arr[middle_index] if len(arr) % 2 == 1 else (arr[middle_index - 1] + arr[middle_index]) / 2
    return median

def get_mode(arr):
    freq_dict = {}

    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    mode = None
    frequency = 0

    for k, v in freq_dict.items():
        if v > frequency:
            frequency = v
            mode = k

    return mode

n = input()
arr = list(map(int, input().split()))
arr.sort()

print(f"{get_mean(arr):.1f}")
print(f"{get_median(arr):.1f}")
print(get_mode(arr))