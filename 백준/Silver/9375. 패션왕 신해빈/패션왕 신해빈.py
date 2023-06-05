import sys
input = sys.stdin.readline

for i in range(int(input())):
    arr = {}
    for k in range(int(input())):
        A, B = input().split()
        if B not in arr.keys():
            arr[B] = str(1)
        else:
            arr[B] += str(1)
                
    counter = 1
    
    for k in arr:
        counter *= (len(arr[k]) + 1)
    
    print(counter - 1)