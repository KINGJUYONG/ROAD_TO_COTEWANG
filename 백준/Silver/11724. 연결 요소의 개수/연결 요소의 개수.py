import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M  = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(id):
    visited[id] = 1
    
    for i in arr[id]:
        if visited[i] == 0:
            dfs(i)

i = 1
counter = 0
while(True):
    if visited.count(1) == N:
        print(counter)
        break
    counter += 1
    dfs(i)
    
    for k in range(1, N+1):
        if visited[k] == 0:
            i = k
            break