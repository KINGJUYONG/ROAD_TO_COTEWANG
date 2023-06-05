import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = list(map(int, input().split()))
k = int(input())

result = []

for i in range(0, N, N // k): # 1 2 3
    result += sorted(arr[i:i+N//k])
                
for i in result:
    print("%d " % i)