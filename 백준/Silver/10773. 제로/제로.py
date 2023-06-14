import sys
from  collections import deque
input = sys.stdin.readline

def solve():
    K = int(input())
    #arr = deque()
    summary = []
    for i in range(K):
        Ap = int(input())
        #arr.append(Ap)
        if Ap != 0:
            summary.append(Ap)
        else:
            summary.pop()
    print(sum(summary))

solve()