from sys import stdin
from fractions import Fraction
input = stdin.readline

n, m = map(int, input().split())
nfac = 1
rfac = 1
nrfac = 1
for i in reversed(range(1, n+1)):
    nfac *= i
for i in reversed(range(1, m+1)):
    rfac *= i
for i in reversed(range(1, n-m+1)):
    nrfac *= i
    
print(Fraction(nfac, (rfac * nrfac)))