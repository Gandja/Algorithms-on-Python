import math

x = 1e-10
a = 0.5


def predel(x, a):
    return math.cos(x ** 0.5) ** (1 / a / x)


print(predel(x, a))
print(1/math.exp(1))
