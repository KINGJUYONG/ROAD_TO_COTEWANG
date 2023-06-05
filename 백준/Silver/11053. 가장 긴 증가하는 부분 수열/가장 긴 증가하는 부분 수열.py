import sys

L = int(sys.stdin.readline().rstrip())

A = []

A = list(map(int, sys.stdin.readline().split()))

ans = [1 for _ in range(L)]

for i in range(1, L):
    for k in range(i):
        if A[i] > A[k]:
            ans[i] = max(ans[i], ans[k]+1)

print(max(ans))