import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    pw = {}
    for i in range(N):
        A, B = input().rstrip().split()
        pw[A] =  B
        
    for i in range(M):
        A = input().rstrip()
        print(pw[A])