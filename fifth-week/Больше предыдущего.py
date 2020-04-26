a = input().split()
number = int(a[0])
for i in range(1, len(a)):
    if int(a[i]) > number:
        print(a[i], end=' ')
    number = int(a[i])
