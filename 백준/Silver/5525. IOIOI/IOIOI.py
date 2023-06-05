import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

arr = 'I'
arr += 'OI' * N
    
lenofIOI = 1 + N * 2

M = int(input())
S = input().rstrip()

counter = 0
for i in range(M-(N*2)):
    if S[i:i+lenofIOI] == arr:
        counter += 1
        i += 1
        
print("%d" % counter)