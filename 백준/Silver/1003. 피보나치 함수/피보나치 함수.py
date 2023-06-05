import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

dp = [[0 for _ in range(41)] for _ in range(2)]

dp[0][0] = 1
dp[1][1] = 1
dp[0][2] = 1
dp[1][2] = 1

for i in range(3, 41):
    dp[0][i] = dp[0][i-1] + dp[0][i-2]
    dp[1][i] = dp[1][i-1] + dp[1][i-2]

for i in range(T):
    a = int(input())
    print("%d " % dp[0][a] )
    print("%d\n" % dp[1][a])