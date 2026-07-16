class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        


        def dfs(i, memo):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0
            count = dfs(i + 1, memo)

            if i + 1 < len(s):
                if s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456':
                    count += dfs(i + 2, memo)
            memo[i] = count
            return memo[i]
        return dfs(0, {len(s): 1})

            







        










        