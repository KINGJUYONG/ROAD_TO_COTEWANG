import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
#print = sys.stdout.write


N = int(input())
G = int(input())

arr = [[]for _ in range(N+1)]
        

for i in range(G):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

counter = 0
visited = [0 for _ in range(N+1)]

def dfs(start):
    global counter
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)
            counter += 1

dfs(1)
print(counter)