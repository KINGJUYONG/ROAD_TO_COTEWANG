import sys

case = int(sys.stdin.readline().rstrip())

for i in range(case):
    test = sys.stdin.readline().rstrip()

    point = 0
    asc = 0
    for k in range(len(test)):
        if test[k] == 'O':
            point += 1 + asc
            asc += 1
        elif test[k] == 'X':
            asc = 0

    print(point)