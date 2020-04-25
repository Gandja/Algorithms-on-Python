x = int(input())
y = int(input())
day = 1
distance = x
while distance < y:
    x = distance
    x = x * 0.1
    distance = distance + x
    day = day + 1
print(day)
