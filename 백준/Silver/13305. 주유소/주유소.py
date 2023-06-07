import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))

gas = gas[0:-1]

cost = 0
flip = 0

mingas = min(gas)

for i in range(N-1):
    if flip == 1:
        flip = 0
        continue
    if gas[i] == mingas:
        cost += sum(dist[i:]) * gas[i]
        break
    elif gas[i] < gas[i+1]:
        cost += sum(dist[i:i+2]) * gas[i]
        flip = 1
    else:
        cost += dist[i] * gas[i]
print(cost)