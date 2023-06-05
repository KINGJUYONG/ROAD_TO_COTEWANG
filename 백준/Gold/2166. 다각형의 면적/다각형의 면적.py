import sys
input = sys.stdin.readline

N = int(input().rstrip())
xy = []

for i in range(N):
    xy.append(list(map(int, input().split())))
    
answer = 0

for i in range(1, N):
    answer += xy[i-1][0] * xy[i][1] - xy[i][0] * xy[i-1][1]
    
answer += xy[N-1][0] * xy[0][1] - xy[0][0] * xy[N-1][1]

print(abs(answer / 2))