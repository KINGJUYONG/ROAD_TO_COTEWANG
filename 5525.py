import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
M = int(input())
S = input().rstrip()

counter, i, res = 0, 0, 0

while (i < M-1):
    if S[i:i+3] == 'IOI':
        counter += 1
        i += 2
        if counter == N:
            res += 1
            counter -= 1
    else:        
        i += 1
        counter = 0
        
print("%d" % res)