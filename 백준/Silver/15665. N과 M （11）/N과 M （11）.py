import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))

for i in itertools.product(arr, repeat = M):
    print(*i)