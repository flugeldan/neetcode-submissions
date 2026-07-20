class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(i, cur):
            cur.append(i)
            if len(cur) == k:
                ans.append(cur.copy())
                cur.pop()
                return
            for j in range(i + 1, n + 1):
                dfs(j, cur)
            
            cur.pop()
        for i in range(1, n + 1):
            dfs(i, [])
        
        return ans




