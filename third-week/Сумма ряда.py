n = int(input())
count = 1
s = 0
while n > 0:
    s += 1 / (count ** 2)
    count += 1
    n -= 1
print(s)
