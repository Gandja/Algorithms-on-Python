a = input().split()
number = 1000
for i in range(0, len(a)):
    if 0 < int(a[i]) <= number:
        number = int(a[i])
print(number)
