import sys

n = int(sys.stdin.readline().rstrip())
tri = [[0 for _ in range(n)] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]

tri[0] = list(map(int, sys.stdin.readline().split()))
ans[0] = tri[0]
if n != 1:
    for i in range(1, n):
        tri[i] = list(map(int, sys.stdin.readline().split()))
        for k in range(i+1):
            if k != 0 and k != i:
                ans[i][k] = max(ans[i-1][k-1], ans[i-1][k]) + tri[i][k]
            elif k == 0:
                ans[i][k] = ans[i-1][k] + tri[i][k]
            else:
                ans[i][k] = ans[i-1][k-1] + tri[i][k]
    print(max(ans[n-1]))


else:
    print(tri[0][0])