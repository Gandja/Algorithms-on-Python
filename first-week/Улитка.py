H = int(input())
A = int(input())
B = int(input())
step = A - B
lastDay = (H - A)
print(((lastDay + (step - 1)) // step) + 1)
