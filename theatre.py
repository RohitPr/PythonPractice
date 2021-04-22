import math

number = input()

number = number.split()

length = int(number[0])
width = int(number[1])
square = int(number[2])


if length % square == 0 and width % square == 0:
    count = int(length/square + width/square)
else:
    count = math.ceil(length/square) + math.ceil(width/square)
print(count)
