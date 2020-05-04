m = int(input())
a = list(map(int, input().split()))

first_list = list()
first_set = set()

for i in a:
    if i in first_set:
        continue
    else:
        first_list.append(i)
        first_set.add(i)
print(len(first_list))
print(*first_list)
