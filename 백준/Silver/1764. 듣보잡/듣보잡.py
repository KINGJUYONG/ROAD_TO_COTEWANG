import sys
input = sys.stdin.readline

N, M = map(int, input().split())

deut = []
bo = []

for i in range(N):
    deut.append(input().rstrip())

for i in range(M):
    bo.append(input().rstrip())

deutbo = sorted(list(set(deut) & set(bo)))


print(len(deutbo))
for i in range(len(deutbo)):
    print(deutbo[i])