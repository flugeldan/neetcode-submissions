class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        def dfs(i, cur, memo):
            if (i, cur) in memo:
                return memo[(i, cur)]
            if i >= len(s):
                return False
            cur += s[i]
            if cur in wordDict:
                if i == len(s) - 1:
                    return True
                memo[(i, cur)] = max(dfs(i + 1, '', memo), dfs(i + 1, cur, memo))
                return memo[(i, cur)]
            memo[(i, cur)] = dfs(i + 1, cur, memo)
            return memo[(i, cur)]



        return dfs(0, '', {})

            

        