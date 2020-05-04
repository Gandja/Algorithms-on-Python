length = int(input())
width = int(input())
height = int(input())

length1 = int(input())
width1 = int(input())
height1 = int(input())

count1 = (length // length1) * (width // width1) * (height // height1)
count2 = (length // length1) * (width // height1) * (height // width1)
count3 = (length // height1) * (width // length1) * (height // width1)
count4 = (length // height1) * (width // width1) * (height // length1)
count5 = (length // width1) * (width // height1) * (height // length1)
count6 = (length // width1) * (width // length1) * (height // height1)

print(max(max(max(count1, count2), max(count3, count4)), max(count5, count6)))
