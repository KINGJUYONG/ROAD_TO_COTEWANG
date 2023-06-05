a = input()
for i in range(0, len(a)):
    if a[i].isupper() == True:
        print(a[i].lower(), end = "")
    else:
        print(a[i].upper(), end = "")