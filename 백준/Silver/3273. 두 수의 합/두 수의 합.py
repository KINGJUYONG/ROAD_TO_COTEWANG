import sys
import itertools
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

counter = 0

left, right = 0, 1

while(left + right != n):
    if arr[left] + arr[-right] == x:
        counter += 1
    
    if arr[left] + arr[-right] < x:
        left += 1
    else:
        right += 1    
    
print(counter)