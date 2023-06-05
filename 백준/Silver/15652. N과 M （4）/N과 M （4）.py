import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())

su = [i for i in range(1, N+1)]

for i in itertools.combinations_with_replacement(su, M):
    for k in range(len(i)):
        print(i[k], end=' ')
    print("")
