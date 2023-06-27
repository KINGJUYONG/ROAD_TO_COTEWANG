import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, k):
    queue = [(i, k)]
    arr[i][k] = 0
    
    while queue:
        i, k = queue.pop(0)
        
        for q in range(4):
            nx = i + dx[q]
            ny = k + dy[q]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 0
            
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(N+1)] for _ in range(M+1)]
    counter = 0
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1
    
    for i in range(M):
        for k in range(N):
            if arr[i][k] == 1:
                bfs(i, k)
                counter += 1
    print(counter)