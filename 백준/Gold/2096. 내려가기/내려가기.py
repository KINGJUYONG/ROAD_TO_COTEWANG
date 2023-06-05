import sys
input = sys.stdin.readline

N = int(input().rstrip())
q = []
maxdp = [0 for _ in range(3)]
mindp = [0 for _ in range(3)]

q.append(list(map(int, input().split())))
mindp[0] = maxdp[0] = q[0]
for i in range(1, N):
    q[0] = (list(map(int, input().split())))
    maxdp[0] = [(max(maxdp[0][0], maxdp[0][1])) + q[0][0], (max(maxdp[0][0], maxdp[0][1], maxdp[0][2])) + q[0][1], (max(maxdp[0][1], maxdp[0][2])) + q[0][2]]
    mindp[0] = [(min(mindp[0][0], mindp[0][1])) + q[0][0], (min(mindp[0][0], mindp[0][1], mindp[0][2])) + q[0][1], (min(mindp[0][1], mindp[0][2])) + q[0][2]]

print(max(maxdp[0]), min(mindp[0]))