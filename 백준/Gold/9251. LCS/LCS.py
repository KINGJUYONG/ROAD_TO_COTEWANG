import sys
input = sys.stdin.readline
sys.setrecursionlimit(1001)

A = input().rstrip()
B = input().rstrip()

lena = len(A)
lenb = len(B)

dp = [[0 for _ in range(lenb + 1)]for _ in range(lena + 1)]

counter = 0
for i in range(1, lena + 1):
    for k in range(1, lenb + 1):
        if A[i-1] == B[k-1]:
            dp[i][k] = dp[i-1][k-1] + 1
        else:
            dp[i][k] = max(dp[i-1][k], dp[i][k-1])
print(max(dp[lena]))