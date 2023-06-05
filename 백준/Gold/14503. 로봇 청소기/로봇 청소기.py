from sys import stdin, stdout
input = stdin.readline
#print = stdout.write

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [[0 for _ in range(M)]for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

count = 0

while(True):
    if arr[r][c] == 0:
        arr[r][c] = 2
        count += 1


    if arr[r-1][c] == 0 or arr[r+1][c] == 0 or arr[r][c-1] == 0 or arr[r][c+1] == 0:
        d -= 1

        if d == 2:
            if arr[r+1][c] == 0:
                r += 1
        elif d == 1:
            if arr[r][c+1] == 0:
                c += 1
        elif d == 0:
            if arr[r-1][c] == 0:
                r -= 1
        elif d < 0:
            d = 3
            if arr[r][c-1] == 0:
                c -= 1
                
        continue


    else:
        if d == 3:
            if arr[r][c+1] != 1:
                c += 1
                continue
            else:
                break
        elif d == 2:
            if arr[r-1][c] != 1:
                r -= 1
                continue
            else:
                break
        elif d == 1:
            if arr[r][c-1] != 1:
                c -= 1
                continue
            else:
                break
        elif d == 0:
            if arr[r+1][c] != 1:
                r += 1
                continue        
            else:
                break
     
print(count)