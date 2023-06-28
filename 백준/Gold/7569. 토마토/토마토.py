import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = [[[0 for _ in range(M)]for _ in range(N)]for _ in range(H)]
for i in range(H):
    for k in range(N):
        arr[i][k] = list(map(int, input().split()))

pcheck = 0
queue = deque([])
for j in range(H):
    for i in range(N):
        for k in range(M):
            if arr[j][i][k] == 1:
                queue.append((j, i, k))



dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
checked = 0

def bfs():
    global checked
    while queue:
        z, y, x = queue.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H:
                continue
            if arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                queue.append((nz, ny, nx))
                checked += 1
                
            

bfs()

maximum = 0
for j in range(H):
    for i in range(N):
        for k in range(M):
            maximum = max(maximum, arr[j][i][k])
            if arr[j][i][k] == 0:
                print(-1)
                exit()
if checked == 0:
    print(0)
    exit()
print(maximum - 1)