import sys

H,M = map(int, sys.stdin.readline().split())
if H > -1 and H < 24 and M > -1 and M < 60:
    if M < 45:
        if H > 0:
            M = M + 15
            H = H - 1
        else:
            H = H + 23
            M = M + 15
    else:
        M = M - 45

    print(H, M)
