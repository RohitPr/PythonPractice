class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        b = ''
        for i in range (len(s)):
            b = s[i:]+s[:i]
            if(b==goal):
                return True
        return False             
    
#     for i in range (len(s)):
#             s = s[1:]+s[:1]
#             if(s==goal):
#                 return True
#         return False     