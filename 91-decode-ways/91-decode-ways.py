class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        
        for a in range(len(s)-1, -1, -1):
            if s[a] == "0":
                dp[a] = 0
            else:
                dp[a] = dp[a+1]
            
            if (a + 1 < len(s) and ( s[a] == '1' or s[a] == '2' and s[a + 1] in "0123456")):
                dp[a] += dp[a+2]
            
        return dp[0]