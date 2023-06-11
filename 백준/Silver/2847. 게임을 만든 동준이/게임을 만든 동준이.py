import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

counter = 0
for i in range(2, N+1):
    #print(arr[-i], arr[-i + 1])
    if arr[-i] >= arr[-i + 1]:
        while(arr[-i] >= arr[-i + 1]):
            arr[-i] -= 1
            counter += 1
print(counter)