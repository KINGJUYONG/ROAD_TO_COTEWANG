import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = sorted(list(map(int, input().split())))

count, i = 1, 0
check = 0

for k in range(1, N):
    if arr[i] + L >= arr[k] + 1:
        check += 1
        continue
    else:
        i += 1 + check
        check = 0
        count += 1
print(count)