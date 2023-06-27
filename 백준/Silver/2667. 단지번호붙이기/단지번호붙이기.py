import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, k):
    queue = [(i, k)]
    arr[i][k] = 0
    counter = 1
    
    while queue:
        i, k = queue.pop(0)
        
        for q in range(4):
            nx = k + dx[q]  
            ny = i + dy[q]
        
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if arr[ny][nx] == 1:
                queue.append((ny, nx))
                arr[ny][nx] = 0
                counter += 1
    return counter
    

N = int(input())
arr = []
result = []
for _ in range(N):
    arr.append(list(map(int, str(input().rstrip()))))
for i in range(N):
    for k in range(N):
        if arr[i][k] == 1:
            result.append(bfs(i, k))
            
print(len(result))
result = sorted(result)
while result:
    print(result.pop(0))