import statistics as st

n = input()
arr = list(map(int, input().split()))

print(st.mean(arr))
print(st.median(arr))
print(min(st.multimode(arr)))