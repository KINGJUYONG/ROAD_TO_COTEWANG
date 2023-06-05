from collections import deque

N = int(input())

q = deque()

for i in range(1, N+1):
    q.append(i)

for _ in range(N-1):
    q.popleft()
    A = q.popleft()
    q.append(A)
    
print(*q)