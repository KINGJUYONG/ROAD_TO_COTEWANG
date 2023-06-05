import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

N, M, R = map(int, input().split())
gan = [[]for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
count = 0

for _ in range(M):
    A, B = map(int, input().split())
    gan[A].append(B)
    gan[B].append(A)
    
for i in range(len(gan)):
    gan[i] = sorted(gan[i])


def dfs(R):
    global count
    count += 1
    visited[R] = count
    for x in gan[R]:
        if visited[x] == 0:
            dfs(x)

dfs(R)

for i in range(1, N+1):
    print(visited[i])