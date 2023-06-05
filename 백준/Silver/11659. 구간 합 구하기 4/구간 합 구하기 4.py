import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

arr = list(map(int, input().split()))

sumsum = 0
sumA = [0]

for i in arr:
    sumsum += i
    sumA.append(sumsum)
    

for i in range(M):
    a, b = map(int, input().split())
    print("%d\n" % int(sumA[b] - sumA[a-1]))