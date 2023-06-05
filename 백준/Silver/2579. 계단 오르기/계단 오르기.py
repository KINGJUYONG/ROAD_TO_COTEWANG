import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
arr = []
dp = [0 for _ in range(N)]
for i in range(N):
    arr.append(int(input()))
    
if len(arr) <= 2:
    print("%d" % sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
    print("%d" % dp[-1])