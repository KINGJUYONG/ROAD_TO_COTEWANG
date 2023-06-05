import sys
import math

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    if distance < 3:
        print(distance)
    else:        
        warped = 0
        root = math.floor(math.sqrt(distance))
        warped += root * 2 - 1
        distance = distance - root * root
        warped += math.ceil(distance / root)
        print(warped)