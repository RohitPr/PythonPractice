import os
import string


def solve(s):
    cap = string.capwords(s, sep=" ")
    return cap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
