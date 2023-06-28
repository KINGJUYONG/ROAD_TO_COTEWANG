from sys import stdin, stdout
from collections import deque
input = stdin.readline
queue = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        verti, hori = queue.popleft()
        for i in range(4):
            nx = hori + dx[i]
            ny = verti + dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if arr[ny][nx] == 0:
                arr[ny][nx] = arr[verti][hori] + 1
                queue.append((ny, nx))
        

M, N = map(int, input().split())

arr = []

summary = 0
for i in range(N):
    arr.append(list(map(int, input().split())))

    
    
    
counter = 0
for i in range(N):
    for k in range(M):
        if arr[i][k] == 1:
            queue.append((i, k))

counter = 0
for i in arr:
    if 0 not in i:
        counter += 1
if counter == N:
    print(0)
    exit()
           
bfs()

maximum = 0

for i in arr:
    if 0 in i:
        print(-1)
        exit()
    if maximum < max(i):
        maximum = max(i)
    
print(maximum - 1)