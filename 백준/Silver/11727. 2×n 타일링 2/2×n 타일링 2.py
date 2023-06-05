import sys
input = sys.stdin.readline

N = int(input())

dp = [0,1,3,5,11]

for i in range(5, N+1):
    dp.append(dp[i-2] * 2 + dp[i-1])

print(dp[N] % 10007)