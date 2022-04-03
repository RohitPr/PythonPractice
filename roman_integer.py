# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
                res -= roman_dict[s[i]]
            else:
                res += roman_dict[s[i]]
        return res
