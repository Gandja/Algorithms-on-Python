n = int(input())
a = list(map(int, input().split()))
x = int(input())
minimum = abs(a[0] - x)
index = a[0]
for i in range(len(a)):
    if a[i] == x:
        print(x)
        exit()
    elif abs(a[i] - x) < minimum:
        minimum = abs(x - abs(a[i]))
        index = a[i]
print(index)
