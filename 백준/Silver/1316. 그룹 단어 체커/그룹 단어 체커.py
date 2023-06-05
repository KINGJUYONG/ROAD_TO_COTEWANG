import sys

N = int(sys.stdin.readline().rstrip())
count = 0

for i in range(N):
    word = str(sys.stdin.readline().rstrip())
    wordlen = len(word)
    if wordlen == 1:
        continue
    else:
        pedal = 0
        for i in reversed(word):
            if word.index(i) != word.rfind(i) and word.rfind(i) - word.index(i) > 1:
                for k in range(word.index(i), word.rfind(i)):
                    if word[k] != i:
                        count = count + 1
                        pedal = pedal + 1
                        break
                if pedal != 0:
                    break
    
print(N - count)