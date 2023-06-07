import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))

gas = gas[0:-1]

cost = 0
for i in range(N-1):
    if gas[i] == min(gas):
        cost += sum(dist[i:]) * gas[i]
        break
    else:
        cost += dist[i] * gas[i]
print(cost)