import sys

N = int(sys.stdin.readline().rstrip())

sum = 0
count = 0

if N < 1001:

    arr = []

    arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))


    for i in range(0, len(arr)):
        if arr[i] < 0 or arr[i] > 100:
            
            break
        else:
            sum += arr[i] / max(arr) * 100
            count = count + 1

if count == N:
    print(sum / N)
