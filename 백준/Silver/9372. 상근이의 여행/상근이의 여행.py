import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        arr[A].append(B)
        arr[B].append(A)
        visited = [0] * (N+1)
        
        def DFS(id, cnt):
            visited[id] = 1
            for i in arr[id]:
                if visited[i] == 0:
                    cnt = DFS(i, cnt+1)
            return cnt
        
    print(DFS(1,0))