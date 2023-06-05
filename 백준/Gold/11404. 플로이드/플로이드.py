import sys
input = sys.stdin.readline
print = sys.stdout.write

INF = int(1e9)

n = int(input().rstrip())
m = int(input().rstrip())

buses = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    buses[a][b] = min(buses[a][b], c)

for i in range(1, n+1):
    for k in range(1, n+1):
        for q in range(1, n+1):
            if k == q:
                buses[k][q] = 0
            else:
                buses[k][q] = min(buses[k][q], buses[k][i] + buses[i][q])

for i in range(1, n+1):
    for k in range(1, n):
        if buses[i][k] == INF:
            print("%d " % 0)
        else:
            print("%d " % buses[i][k])
    if buses[i][n] == INF:
        print("%d\n" % 0)
    else:
        print("%d\n" % buses[i][n])