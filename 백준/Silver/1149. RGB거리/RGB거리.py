import sys

N = int(sys.stdin.readline().rstrip())

amount = [[0 for _ in range(3)]  for _ in range(N)]

pointer = 0

for i in range(N):
    amount[i] = list(map(int, sys.stdin.readline().split()))
    amount[i][0] = min(amount[i-1][1], amount[i-1][2]) + amount[i][0]
    amount[i][1] = min(amount[i-1][2], amount[i-1][0]) + amount[i][1]
    amount[i][2] = min(amount[i-1][0], amount[i-1][1]) + amount[i][2]

print(min(amount[N-1][0], amount[N-1][1], amount[N-1][2]))