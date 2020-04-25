A = int(input())
B = int(input())
N = int(input())
price = A * 100 + B
print(int(price * N / 100), (price * N) % 100)
