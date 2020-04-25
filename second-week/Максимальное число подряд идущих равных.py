n = int(input())
count = 1
maxCount = 0
maximum = 0
while n != 0:
    if n == maximum:
        count += 1
    if n != maximum:
        count = 1
        maximum = 0
    if n > maximum:
        count = 1
        maximum = n
    if count > maxCount:
        maxCount = count
    n = int(input())
print(maxCount)
