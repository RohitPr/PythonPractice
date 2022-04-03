# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


def solution(s):
    length = len(s)
    split_list = []

    if length % 2 != 0:
        s += "_"
        length += 1

    for a in range(0, length, 2):
        split_list.append(s[a:a+2])

    return split_list


print(solution('abcd'))
