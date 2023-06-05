from sys import stdin, stdout
import itertools

input = stdin.readline
print = stdout.write

N, M = map(int, input().split())
arr = list(map(int, input().split()))
   
arr = sorted(arr)
    
tmp = set([])

for i in itertools.permutations(arr, M):
    if i not in tmp:
        for k in range(len(i)):
            print("%d " % i[k])
        print("\n")
        tmp.add(i)