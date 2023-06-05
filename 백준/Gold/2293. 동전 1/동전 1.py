import sys
import itertools

n, k = map(int, sys.stdin.readline().split())

amount_coin = [0] * n

for i in range(n):
    amount_coin[i] = int(sys.stdin.readline().rstrip())
amount_coin.sort()

count = [0] * 10001
count[0] = 1

for i in range(0, n):
    for j in range(amount_coin[i], k+1):
        count[j] += count[j - amount_coin[i]]

print(count[k])