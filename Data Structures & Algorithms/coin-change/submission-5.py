class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        #step 1 take coin and take it again
        #step 2 take coin and go to the next coin
        #step 3 just go to the next coin
        def dfs(rem):
            if rem == 0:
                return 0 
            elif rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            beststep = float('inf')
            for c in coins:
                beststep = min(beststep, 1 + dfs(rem - c))
            memo[rem] = beststep
            return memo[rem] 
        ans = dfs(amount) 
        return ans if ans != float('inf') else -1



