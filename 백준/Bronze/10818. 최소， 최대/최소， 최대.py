import sys

N = int(sys.stdin.readline().rstrip())
inte = []
if N > 0 and N < 1000001:
    inte = (list(map(int, sys.stdin.readline().split())))
    check = 0
    for i in range(0, len(inte)):
        if inte[i] < -1000000 and inte[i] > 1000000:
            check = 1
    if check == 0:
        print(min(inte), max(inte))
