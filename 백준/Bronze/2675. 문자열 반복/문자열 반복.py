import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    R, S = sys.stdin.readline().split()

    for k in range(len(S)):
        for i in range(int(R)):
            print(S[k], end='')
    print("")