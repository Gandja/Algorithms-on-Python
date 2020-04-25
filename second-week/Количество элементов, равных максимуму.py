n = int(input())
count = 1
maximum = 0
while n != 0:
    if n > maximum:
        count = 1
        maximum = n
    elif n == maximum:
        count += 1
    n = int(input())
print(count)
