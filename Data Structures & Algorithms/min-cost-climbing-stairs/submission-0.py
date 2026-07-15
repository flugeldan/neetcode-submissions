class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def brbr(i, memo):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(brbr(i + 1, memo), brbr(i + 2, memo))
            return memo[i]
        return min(brbr(0, {}), brbr(1, {}))


