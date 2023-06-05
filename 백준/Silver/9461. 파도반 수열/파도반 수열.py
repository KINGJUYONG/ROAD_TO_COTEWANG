import sys
input = sys.stdin.readline
print = sys.stdout.write


dp = [0,1,1,1,2,2]

for i in range(6, 101):
    dp.append(dp[i-1] + dp[i-5])

T = int(input())
for i in range(T):
    N = int(input())
    print("%d\n" % dp[N])