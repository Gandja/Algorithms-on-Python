def rev():
    n = int(input())
    if n == 0:
        return print(n)
    rev()
    return print(n)


rev()
