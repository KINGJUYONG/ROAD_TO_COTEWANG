import sys
import itertools

N, M = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

for i in itertools.permutations(nums, M):
    for k in range(len(i)):
        print(i[k], end=' ')
    print()