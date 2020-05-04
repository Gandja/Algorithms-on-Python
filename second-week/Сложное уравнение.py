a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    print('INF')
elif a == 0 and b != 0:
    print('NO')
else:
    x = -b / a
    if c * x + d == 0 or x % 1 != 0:
        print('NO')
    else:
        print(int(x))
