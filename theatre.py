number = input()

number = number.split()

length = int(number[0])
width = int(number[1])
square = int(number[2])

if length == 1 and width == 1:
    count = 1
elif length % square == 0 and width % square == 0:
    count = int(length/square * width/square)
else:
    count = round(length/square) + round(width/square)
print(count)
