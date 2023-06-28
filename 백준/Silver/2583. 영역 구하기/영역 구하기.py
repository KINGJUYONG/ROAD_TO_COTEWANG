import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(vert, hori):
    queue = [(vert, hori)]
    counter = 1
    arr[vert][hori] = 0
    
    while queue:
        vert, hori = queue.pop(0)
        
        for i in range(4):
            nx = hori + dx[i]
            ny = vert + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if arr[ny][nx] == 1:
                queue.append((ny, nx))
                counter += 1
                arr[ny][nx] = 0
    return counter

M, N, K = map(int, input().split())
arr = [[1 for _ in range(N)]for _ in range(M)]
for _ in range(K):
    A, B, C, D = map(int, input().split())
    for i in range(B, D):
        for k in range(A, C):
            arr[i][k] = 0

result = []
for i in range(M):
    for k in range(N):
        if arr[i][k] == 1:
            result.append(bfs(i, k))
            
print(len(result))
print(*sorted(result))