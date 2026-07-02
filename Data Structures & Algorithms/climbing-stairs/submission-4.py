class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]

        for _ in range(n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[1]