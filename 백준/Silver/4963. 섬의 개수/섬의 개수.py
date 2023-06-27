import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(x, y):
    queue = [(x, y)]
    island[y][x] = 0
    
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(8):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                continue
            #print(nx, ny)
            if island[ny][nx] == 1:
                queue.append((nx, ny))
                island[ny][nx] = 0
    


while(True):
    W, H = map(int, input().rstrip().split())
    if W == 0 and H == 0:
        break
    counter = 0
    island = []
    for i in range(H):
        island.append(list(map(int, input().split())))
    
    #print(island)
    
    for i in range(H):
        for k in range(W):
            if island[i][k] == 1:
                bfs(k, i)
                counter += 1
    print(counter)