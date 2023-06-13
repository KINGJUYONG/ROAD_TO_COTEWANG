import sys
import itertools
input = sys.stdin.readline
#print = sys.stdout.write

N, M = map(int, input().split())

arr = [1 for _ in range(M)]

while(True):
    print(*arr)
    arr[-1] += 1
    if sum(arr) == N*M + 1:
        break
    for i in range(1, M+1):
        if arr[-i] > N:
            arr[-i-1] += 1
            arr[-i] = 1
#print(arr)