import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
A = []
A = sys.stdin.readline().rstrip().split()

for i in range(len(A)):
    if int(A[i]) < X:
        print(A[i], end=' ')