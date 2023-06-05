a = int(input())
for i in range(0, a + 1):
    for k in range(0, i):
        if(k == i - 1):
            print("*", end='\n')
        else:
            print("*", end='')