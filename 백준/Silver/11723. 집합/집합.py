import sys
input = sys.stdin.readline
#print = sys.stdout.write

M = int(input())

S = []

for i in range(M):
    msg = input().rstrip()
    
    if msg[-1].isdigit() == True:
        msg, integer = msg.split()
        integer = int(integer)
        
    if msg == 'add':
        if integer not in S:
            S.append(integer)
    elif msg == 'remove':
        if integer in S:
            S.remove(integer)
    elif msg == 'check':
        if integer in S:
            print(1)
        else:
            print(0)    
    elif msg == 'toggle':
        if integer in S:
            S.remove(integer)
        else:
            S.append(integer)
    elif msg == 'all':
        S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif msg == 'empty':
        S = []