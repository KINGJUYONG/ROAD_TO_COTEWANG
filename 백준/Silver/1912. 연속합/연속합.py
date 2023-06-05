import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [-1001 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = max(arr[i-1], dp[i-1] + arr[i-1])
    
print(max(dp))