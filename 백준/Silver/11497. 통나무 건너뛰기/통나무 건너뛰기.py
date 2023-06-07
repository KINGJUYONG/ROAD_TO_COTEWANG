import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    
    maximum = 0
    
    for i in range(2, N):
        maximum = max(maximum, abs(arr[i] - arr[i-2]))
        
    print(maximum)
    
    # tmparr = sorted(arr[0:N//2])
    # tmparr += sorted(arr[N//2:], reverse=True)
    
    # print(tmparr)
    
    # maximum = abs(tmparr[0] - tmparr[N-1])
    # for i in range(1, N-1):
    #     maximum = max(abs(tmparr[i] - tmparr[i+1]), maximum)
    # print(maximum)