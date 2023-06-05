import sys

user = int(sys.stdin.readline().rstrip())

for i in range(0, user):
    A,B = map(int, sys.stdin.readline().split())
    print(A + B)
