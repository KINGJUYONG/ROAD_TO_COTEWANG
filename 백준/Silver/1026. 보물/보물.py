import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B.sort(reverse=True)

summary = 0
for i in range(N):
    summary += A[i] * B[i]
print(summary)