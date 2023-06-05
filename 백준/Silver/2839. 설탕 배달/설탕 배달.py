import sys
input = sys.stdin.readline

N = int(input())

counter = 0

while N >= 0:
    if N % 5 == 0:
        counter += N // 5
        print(counter)
        break
    N -= 3
    counter += 1
else:
    print(-1)