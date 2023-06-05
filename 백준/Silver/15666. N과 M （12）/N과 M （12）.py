import itertools
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

confirm = set([])

for i in itertools.combinations_with_replacement(arr, M):
    if i not in confirm:
        for k in range(len(i)):
            print("%d " % i[k])
        print("\n")
        confirm.add(i)