class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        countT, window = {}, {}
        
        for a in t:
            countT[a] = 1 + countT.get(a, 0)
        
        l = 0

        res, resLen = "", float("infinity")
        have, need = 0, len(countT)
        
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                # Update the Result
                if (r-l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                
                # Pop from the Left
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                    
                l += 1
                
        return res if resLen < float("infinity") else ""