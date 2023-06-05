import sys
A = []
for i in range(0, 9):
    A.insert(i, int(sys.stdin.readline().rstrip()))
    if A[i] > 100 or A[i] < 0:
        break

print(max(A))
print(A.index(max(A)) + 1)
        
