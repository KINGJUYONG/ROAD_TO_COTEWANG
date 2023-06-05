import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

arr = {}

for i in range(1, N+1):
    arr[i] = (input().rstrip())

arr_rev = {v:k for k,v in arr.items()}

for i in range(M):
    a = input().rstrip()
    if a.isdigit() == True:
        a = int(a)
        print("%s\n" % arr[a])
    else:
        print("%d\n" % arr_rev[a])