count = int(input())
words = []

for a in range(0, count):
    words.append(input())

for word in words:
    length = int(len(word))
    if length < 11:
        print(word)
    else:
        first_char = word[0]
        last_char = word[-1]
        final_count = str(length-2)
        print(first_char+final_count+last_char)
