# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

def numSplits(s: str) -> int:
    s1, s2 = '', ''
    res = 0

    for a in range(len(s)):
        s1 = s[0:a]
        s2 = s[a:len(s)]
        if len(set(s1)) == len(set(s2)):
            res += 1
    return res
