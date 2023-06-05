import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
xn = []
psum = 0
nsum = 0

for loop in range(T): # T번 반복
    rev = 0
    #print(str(loop) + "번 돕니다(T만큼)")
    p = sys.stdin.readline().rstrip() # p는 함수
    lenofp = len(p)
    psum += lenofp
    if nsum < 700001 and psum < 700001: 
        n = int(sys.stdin.readline().rstrip()) # 원소의 갯수 n
        nsum += n
        xn = deque(sys.stdin.readline().rstrip().split(','))
        xn[0] = xn[0].strip("[")
        xn[n-1] = xn[n-1].strip("]")
        err = 0
        for i in range(lenofp):
            #print(str(i) + "번 돕니다(함수길이만큼)")
            if p[i] == 'R':
                rev = rev + 1
            elif p[i] == 'D':
                n = n - 1
                if n < 0:
                    print("error")
                    err = 1
                    break
                
                if rev % 2 == 0:
                    xn.popleft()
                else:
                    xn.pop()
            
        if err == 0:
            if rev % 2 != 0:
                xn.reverse()
            print('[' +','.join(map(str, xn)) + ']')
    elif sum > 700000:
        break
