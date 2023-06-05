import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split(' '))
#a 97 e 101 i 105 o 111 u 117
# z 122
array = []
array = sys.stdin.readline().rstrip().split(' ')

aeverified = 0
bcverified = 0
aeiou = ['a','e','i','o','u']

for i in range(C):
    if array[i] in aeiou:
        aeverified = aeverified + 1
    else:
        bcverified = bcverified + 1

if aeverified != 0 and bcverified > 1:
    array.sort()
    ans = list(combinations(array, L))
    for i in range(len(ans)):
        prin = ""
        aeverified = 0
        bcverified = 0
        for k in range(L):
            prin = prin + ans[i][k]
            if ans[i][k] in aeiou:
                aeverified = aeverified + 1
            else:
                bcverified = bcverified + 1
        if aeverified != 0 and bcverified > 1:
            print(prin)
