import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
arr = list(map(int, input().split()))
arr = sorted(arr)
summary = 0
for i in range(N):
    summary += sum(arr[0:i+1])
    
print(summary)