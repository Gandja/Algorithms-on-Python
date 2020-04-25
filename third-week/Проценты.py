p = int(input())
x = int(input())
y = int(input())
deposit = x * 100 + y
percent = p / 100
money = deposit + deposit * percent
print(int(money / 100), int(money % 100))
