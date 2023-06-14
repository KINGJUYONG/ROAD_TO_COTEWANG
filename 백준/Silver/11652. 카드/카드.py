import sys
from collections import Counter
input = sys.stdin.readline
arr = []
for i in range(int(input())):
    arr.append(int(input()))

arr = sorted(arr)

arr = Counter(arr).most_common()

print(arr[0][0])