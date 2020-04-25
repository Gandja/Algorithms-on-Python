def IsPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d <= n ** 0.5:
        if n % d == 0:
            return False
        d += 2
    return True


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
