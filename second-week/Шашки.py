x = int(input())
y = int(input())

x1 = int(input())
y1 = int(input())

if (x + y + x1 + y1) % 2 == 0 and y1 > y and y1 - y >= abs(x1 - x):
    print('YES')
else:
    print('NO')
