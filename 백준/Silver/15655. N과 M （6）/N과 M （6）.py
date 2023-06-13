import sys
import itertools as it
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in it.combinations(arr, M):
    print(*i)