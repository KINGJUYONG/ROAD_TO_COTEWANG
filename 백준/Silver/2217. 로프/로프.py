import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)

maximum = arr[0]
for i in range(1, N):
    maximum = max(maximum, arr[i] * (i+1))
    
print(maximum)