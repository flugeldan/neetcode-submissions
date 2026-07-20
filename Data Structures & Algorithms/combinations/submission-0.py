class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(i, cur, been):
            been.add(i)
            cur.append(i)
            if len(cur) == k:
                ans.append(cur.copy())
                been.discard(i)
                cur.pop()
                return
            for j in range(i + 1, n + 1):
                if j not in been:
                    dfs(j, cur, been)
            
            been.discard(i)
            cur.pop()
        for i in range(1, n + 1):
            dfs(i, [], set())
        
        return ans




