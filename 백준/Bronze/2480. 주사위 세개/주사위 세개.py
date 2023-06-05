import sys

a, b, c= map(int, sys.stdin.readline().split())
money = 0
if a==b and b==c:
    money = 10000 + a * 1000
elif a==b or b==c:
    money = 1000 + b * 100
elif a==c:
    money = 1000 + c * 100
else:
    if a>b and a>c:
        money = a * 100
    elif b > a and b > c:
        money = b * 100
    else:
        money = c * 100

print(money)
