from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]        

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] + arr[i-1][j-1] - dp[i-1][j-1]

for i in range(M):
     a,s,d,f = map(int, input().split(' '))
     result = dp[d][f] - dp[d][s-1] - dp[a-1][f] + dp[a-1][s-1]
     print("%d\n" % result)