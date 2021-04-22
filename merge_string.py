from collections import OrderedDict


def merge_the_tools(string, k):
    l = []
    for i in range(0, len(string), k):
        a = string[i:i+k]
        l.append("".join(OrderedDict.fromkeys(a)))
    for j in range(0, len(l)):
        print(l[j])


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
