import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

print(round(sum(arr)/N))

if N % 2 == 1:
    print(arr[N//2])
elif N > 2:
    print(round((arr[N//2] + arr[N//2 + 1])/2))
else:
    print(round((arr[N//2] + arr[N//2 - 1])/2))

cnt = Counter(arr).most_common()
if N > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

if N > 1:
    if arr[-1] > -1:
        print(arr[-1] - arr[0])
    else:
        print(arr[-1] - arr[0])
else:
    print(0)