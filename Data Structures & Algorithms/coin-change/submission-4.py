class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        #step 1 take coin and take it again
        #step 2 take coin and go to the next coin
        #step 3 just go to the next coin
        def dfs(i, cur):
            if (i, amount - cur) in memo:
                return memo[(i, amount - cur)]
            if cur == amount:
                return 0
            elif cur > amount or i >= len(coins):
                return float('inf')
            
            

            memo[(i, amount - cur)] = min(1 + dfs(i, cur + coins[i]), 1 + dfs(i + 1, cur + coins[i]), dfs(i + 1, cur))
            return memo[(i, amount - cur)]
        ans = dfs(0, 0)
        return ans if ans != float('inf') else -1


   

