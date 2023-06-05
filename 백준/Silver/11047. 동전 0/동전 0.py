import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(input().rstrip()))
    
sum = 0
amount = 0

for i in reversed(coins):
    if i <= K - sum:
        a = int((K-sum) / i)
        sum += i * a
        amount += a
    if sum == K:
        break

print(amount)