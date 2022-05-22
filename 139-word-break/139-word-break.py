class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for a in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (a + len(w)) <= len(s) and s[a : a + len(w)] == w:
                    dp[a] = dp[a + len(w)]
                if dp[a]:
                    break
        return dp[0]