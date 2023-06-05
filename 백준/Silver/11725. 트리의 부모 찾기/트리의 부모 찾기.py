import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input().rstrip())
arr = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def DFS(start, arr, parents):
    for i in arr[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i, arr, parents)
            
DFS(1, arr, parents)

for i in range(2, N+1):
    print(parents[i])