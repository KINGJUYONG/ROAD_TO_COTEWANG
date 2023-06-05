import sys
import bisect
input = sys.stdin.readline
#print = sys.stdout.write

N = int(input())
arr = [0] + list(map(int, input().split()))

listarr = [-float('inf')]
bestarr = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if arr[i] > listarr[-1]:
        listarr.append(arr[i])
        bestarr[i] = len(listarr) - 1
    else:
        bestarr[i] = bisect.bisect_left(listarr, arr[i])
        listarr[bestarr[i]] = arr[i]
        
listlen = int(len(listarr))
print(listlen - 1)
    
LIS = max(bestarr) + 1
result = []

for i in reversed(range(1, N+1)):
    if bestarr[i] == LIS - 1:
        result.append(arr[i])
        LIS = bestarr[i]
        
print(*result[::-1])
