import sys

N = sys.stdin.readline().rstrip()

if int(N) > -1 and int(N) < 100:
        
    counter = 0
    done = 1

    if int(N) < 10:
        ex_a = 0
        ex_b = int(N[0])
    else:
        ex_a = int(N[0])
        ex_b = int(N[1])
    
    ex_sum = ex_a + ex_b

    index_a = ex_b * 10 + int(str(ex_sum)[-1])


    while done == 1:
        index_a = ex_b * 10 + int(str(ex_sum)[-1])
        if int(index_a) > 9:
            ex_a = int(str(index_a)[0])
            ex_b = int(str(index_a)[-1])
        else:
            ex_a = 0
            ex_b = int(str(index_a)[0])

        ex_sum = ex_a + ex_b
        counter = counter + 1

        if index_a == int(N):
            break

        
    print(counter)
