a = float(input())
b = float(input())
c = float(input())
d = (b ** 2 - (4 * a * c))
if d >= 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    if x1 and x2 and x1 != x2:
        if x1 < x2:
            print(x1, x2)
        else:
            print(x2, x1)
    elif x1:
        print(x1)
    elif x2:
        print(x2)
else:
    exit()
