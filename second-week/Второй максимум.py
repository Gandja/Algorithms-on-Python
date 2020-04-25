n = int(input())
maximum = 0
secondMax = 0
while n != 0:
    if n > maximum:
        secondMax = maximum
        maximum = n
    elif secondMax < n <= maximum:
        secondMax = n
    n = int(input())
print(secondMax)
