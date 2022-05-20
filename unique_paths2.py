from math import product


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for i, j in product(range(m), range(n)):
            if obstacleGrid[i][j]:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
        return dp[-1]
