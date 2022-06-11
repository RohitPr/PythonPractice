class Solution:
    _dp = [0]
    def numSquares(self, n: int) -> int:
#         dp = [n] * (n + 1)
#         dp[0] = 0
        
#         for target in range(1, n + 1):
#             for s in range(1, target + 1):
#                 square = s * s
#                 if target - square < 0:
#                     break
#                 dp[target] = min(dp[target], 1 + dp[target - square])
                
#         return dp[n]

    
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
                