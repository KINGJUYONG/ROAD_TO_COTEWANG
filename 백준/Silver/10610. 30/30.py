import sys
input = sys.stdin.readline

N = list(input().rstrip())
N.sort(reverse=True)

num = 0
for i in N:
    num += int(i)
    num *= 10
num //= 10

if num % 30 == 0:
    print(num)
else:
    print(-1)