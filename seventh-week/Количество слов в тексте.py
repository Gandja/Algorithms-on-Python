fileIn = open('input.txt', 'r', encoding='utf-8')
line = str(fileIn.read())
print(len(set(line.strip().split())))
