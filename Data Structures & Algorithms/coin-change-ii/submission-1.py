class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, rem):
            if rem == 0:
                return 1
            elif rem < 0:
                return 0
            elif (i, rem) in memo:
                return memo[(i, rem)]
            
            total = dfs(i, rem - coins[i])

            for c in range(i + 1, len(coins)):
                if rem - coins[c] >= 0:
                    total += dfs(c, rem - coins[c])
            memo[(i, rem)] = total
            return memo[(i, rem)]
        return dfs(0, amount)



        