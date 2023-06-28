import sys
from collections import deque
input = sys.stdin.readline


N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    
dist = [-1 for _ in range(N+1)]

dist[X] = 0

def dfs(X):
    q = deque([X])
    while q:
        now = q.popleft()
        
        for next in arr[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                q.append(next)

dfs(X)
checked = 0
for i in range(1, N+1):
    if dist[i] == K:
        print(i)
        checked += 1
if checked == 0:
    print(-1)