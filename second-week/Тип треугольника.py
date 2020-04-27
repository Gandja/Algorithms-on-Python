a = int(input())
b = int(input())
c = int(input())

cosA = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
cosB = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
cosC = (b ** 2 + a ** 2 - c ** 2) / (2 * b * c)
if (a < c + b) and (b < c + a) and (c < b + a):
    if cosA == 0 or cosB == 0 or cosC == 0:
        print('rectangular')
    elif cosA < 0 or cosB < 0 or cosC < 0:
        print('obtuse')
    elif cosA > 0 or cosB > 0 or cosC > 0:
        print('acute')
else:
    print('impossible')
