import sys
input = sys.stdin.readline

A = input().rstrip()


flag = 0

arr = []

for i in range(len(A)):
    if A[i] == '<':
        if len(arr) > 0:
            for _ in range(len(arr)):
                print(arr.pop(), end = '')
        print(A[i], end = '')
        flag = 1
        continue
    elif A[i] == '>':
        print(A[i], end = '')
        flag = 0
        continue
    elif flag == 1:
        print(A[i], end = '')
        continue
    elif A[i] == ' ':
        for _ in range(len(arr)):
            print(arr.pop(), end = '')
        print(' ', end = '')
    else:
        arr.append(A[i])
        
try:
    for _ in range(len(arr)):
        print(arr.pop(), end = '')
except:
    exit()