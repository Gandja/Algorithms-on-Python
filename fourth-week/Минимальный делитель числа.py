n = int(input())


def MinDivisor(n):
    i = 2
    while n % i != 0:
        i += 1
        if i > n ** 0.5:
            return n
    return i


print(MinDivisor(n))
