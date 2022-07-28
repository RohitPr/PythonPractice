class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

#         count_s = {}
#         count_t = {}

#         temp_s = set(s)

#         for a in temp_s:
#             count_s[a] = s.count(a)
#             count_t[a] = t.count(a)

#         for k, v in count_s.items():
#             if count_s[k] != count_t[k]:
#                 return False

#         return True

        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for a in range(len(s)):
            s1Count[ord(s[a])-ord('a')] +=1
            s2Count[ord(t[a])-ord('a')] +=1
            
        return s1Count == s2Count