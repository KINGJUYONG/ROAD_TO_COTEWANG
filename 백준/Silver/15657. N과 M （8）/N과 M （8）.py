from sys import stdin
import itertools
input = stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

for k in itertools.combinations_with_replacement(arr, M):
    lenk = len(k)
    for i in range(lenk-1):
        print(k[i], end=' ')
    print(k[lenk-1])