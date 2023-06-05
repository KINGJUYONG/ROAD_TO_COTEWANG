import sys
input = sys.stdin.readline

M = int(input())
Marr = list(map(int, input().split()))
Marr = sorted(Marr)
N = int(input())
Narr = list(map(int, input().split()))

# Marr 안에 Narr의 요소들이 존재하는지 출력하는 것

for i in Narr:
    counter, low, high = 0, 0, M-1

    while(low <= high):
        mid = (low + high) // 2
        if Marr[mid] == i:
            print(1)
            counter += 1
            break
        elif (Marr[mid] > i):
            high = mid - 1
        else:
            low = mid + 1
    if counter == 0:
        print(0)