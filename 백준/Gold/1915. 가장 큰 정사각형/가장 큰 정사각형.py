import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, list(input().rstrip()))))
count = 0
for i in range(N):
    for q in range(M):
        if arr[i][q] > 0 and i > 0 and q > 0:
            arr[i][q] += min(arr[i-1][q-1], arr[i][q-1], arr[i-1][q])
        count = max(arr[i][q], count)
            
print(count**2)