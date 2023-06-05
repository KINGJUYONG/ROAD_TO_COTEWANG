import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

if A>99 and A < 1000 and B>99 and B<1000 and C>99 and C < 1000:
    for i in range(0, 10):
        globals()['number_{}'.format(i)] = 0 

    result = A*B*C
    result = str(result)
    for k in range(0, len(result)):
        for q in range(0, 10):
            if int(result[k]) == q:
                globals()['number_{}'.format(q)] = globals()['number_{}'.format(q)] + 1
                break

    for n in range(0, 10):
        print(globals()['number_{}'.format(n)])
