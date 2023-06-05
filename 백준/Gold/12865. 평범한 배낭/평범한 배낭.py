import sys
# N 물건갯수 K 무게

# 물건은
# 무게 가치
N, K = map(int, sys.stdin.readline().split())
matrix = []
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    wei, val = matrix[i-1][0], matrix[i-1][1]       # i번째 물건의 무게, 가치 가져옴
    for j in range(1, K+1):
        if j < wei: # 현재 찾는중인 무게가 i번째의 무게보다 작으면
            dp[i][j] = dp[i-1][j] 
        else:
            dp[i][j] = max(dp[i-1][j-wei]+val, dp[i-1][j])

print(dp[N][K])