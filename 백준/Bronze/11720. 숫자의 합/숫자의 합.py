import sys

A = int(sys.stdin.readline().strip())
amount = 0
if A > 0 and A < 101:
    B = sys.stdin.readline().strip()
    for i in range(0, A):
        amount += int(B[i])

print(amount)
