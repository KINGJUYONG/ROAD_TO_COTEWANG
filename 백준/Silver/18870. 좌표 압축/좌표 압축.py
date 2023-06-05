import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = list(map(int, input().split()))
exc_arr = sorted(list(set(arr)))
dict = {exc_arr[i] : i for i in range(len(exc_arr))}
for i in arr:
    print("%d " % dict[i])