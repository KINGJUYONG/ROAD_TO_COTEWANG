from sys import stdin
input = stdin.readline

A, B, C = list(map(int, input().split()))

def multi(a,b,c):
    if b == 1:
        return (a%c)
    elif b % 2 == 0:
        return (multi(a, b//2, c) ** 2) % c
    else:
        return ((multi(a, b//2, c) ** 2) * a ) % c
    
print(multi(A, B, C))