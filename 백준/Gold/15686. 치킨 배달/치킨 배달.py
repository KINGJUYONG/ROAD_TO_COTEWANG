import sys
import itertools

N, M = map(int, sys.stdin.readline().split())

arr = [[0 for j in range(N)] for i in range(N)]
chicken = []
house = []
dist = []

for i in range (N):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    for k in range(N):
        if arr[i][k] == 0:
            continue
        elif arr[i][k] == 2:
            chicken.append([i,k])
        else:
            house.append([i,k])

lenofhouse = len(house)
lenofchicken = len(chicken)
alldist = [[1000000 for k in range(lenofhouse)] for i in range(lenofchicken)]

best = 100000000

for i in itertools.combinations(chicken, M):
    dist = 0
    for k in range(lenofhouse):
        bestdis = 100000000
        for q in range(M):
            fir = abs(house[k][0] - i[q][0]) + abs(house[k][1] - i[q][1])
            if fir < bestdis:
                bestdis = fir
        dist += bestdis
        
    best = min(dist, best)

print(best)