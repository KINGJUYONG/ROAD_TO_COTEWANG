import sys, itertools
input = sys.stdin.readline
nlen = 1
while(True):
    N = list(map(int, input().split()))
    nlen = N[0]
    if nlen == 0:
        break
    N = N[1:]
    for i in itertools.combinations(N, 6):
        print(*i)
    print()