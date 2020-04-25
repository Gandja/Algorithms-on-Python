number = int(input())
first = number // 1000
second = number % 1000 // 100
third = number % 100 // 10
fourth = number % 10
p1 = (first - fourth) * 7
p2 = (second - third) * 9
print(p1 + p2 + 1)
