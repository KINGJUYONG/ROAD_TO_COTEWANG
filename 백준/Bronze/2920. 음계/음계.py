import sys

music = []
music = sys.stdin.readline().split()

asc = 0
des = 0

for i in range(8):
    if i != 0 and int(music[i-1]) + 1 == int(music[i]):
        asc += 1
    elif int(music[i-1]) - 1 == int(music[i]):
        des += 1

if asc == 7:
    print("ascending")
elif des == 7:
    print("descending")
else:
    print("mixed")