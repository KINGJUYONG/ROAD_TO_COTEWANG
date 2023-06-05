import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, L = map(int, input().split())
arr = list(map(int, input().split()))

lis = deque()

for i in range(N):
    while lis and lis[-1][0] > arr[i]:
        lis.pop()
    while lis and lis[0][1] < i - L + 1:
        lis.popleft()
    lis.append((arr[i], i))
    print("%d " % lis[0][0])