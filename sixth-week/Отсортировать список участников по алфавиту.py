# Известно, что фамилии всех участников — различны.
# Сохраните в массивах список всех участников и выведите его, отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
# Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8').

fin = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf8')
read = fin.readlines()
res = []
for line in read:
    line = line.strip().split()
    res.append(line)
res.sort(key=lambda x: x[0])
for i in res:
    print(i[0], i[1], i[3], file=outFile)
fin.close()
