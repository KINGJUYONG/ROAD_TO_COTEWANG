import sys
import itertools
input = sys.stdin.readline
print = sys.stdout.write

if __name__ == "__main__":
    N = int(input())
    
    for i in range(N):
        A = int(input())
        
        arr = [1, 2, 3]
        
        counter = 0
        
        for i in range(1, A+1):
            for k in itertools.product(arr, repeat = i):
                if sum(k) == A:
                    counter += 1
                    
        print("%d\n" % counter)