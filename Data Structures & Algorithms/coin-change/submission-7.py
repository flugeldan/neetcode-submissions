class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort()
        def dfs(i, rem):
            if rem == 0:
                return 0
            if (i, rem) in memo:
                return memo[(i, rem)]
            take = 1 + dfs(i, rem - coins[i]) if rem - coins[i] >= 0 else float('inf')
            step = dfs(i + 1, rem) if i + 1 < len(coins) and rem - coins[i + 1] >= 0 else float('inf')

            memo[(i, rem)] = min(take, step)
            return memo[(i, rem)] 
        ans = dfs(0, amount)
        if ans == float('inf'):
            return -1
        return ans

            
            


        