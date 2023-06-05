import sys

A = sys.stdin.readline().rstrip()

try:
    print(ord(A))
except:
    print(chr(A))