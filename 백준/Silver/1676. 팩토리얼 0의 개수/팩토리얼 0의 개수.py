import sys
input = sys.stdin.readline

n = int(input())

sum = 1
a = 0    

for i in range(1, n+1):
    sum *= i
    
while(sum % 10 == 0):
    a += 1
    sum = sum // 10

print(a)