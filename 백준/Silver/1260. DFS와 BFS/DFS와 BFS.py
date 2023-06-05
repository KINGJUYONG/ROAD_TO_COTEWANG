import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M, V = map(int,input().split())

arr = [[]for _ in range(N+1)]

for i in range(M):
    A,B = map(int,input().split())
    arr[A].append(B)
    arr[B].append(A)
    
for i in range(N+1):
    arr[i] = sorted(arr[i])

def dfs(start):
    print("%d " % start)
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)
            
def bfs(start):
    global visit, arr
    q = deque([start])
    visit[start] = 1
    
    while(q):
        a = q.popleft()
        print("%d " % a)
        for i in arr[a]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1
    
visited = [0 for _ in range(N+1)]            
dfs(V)
print("\n")
visit = [0 for _ in range(N+1)]
bfs(V)
