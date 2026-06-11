class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        def bfs(i, j):
            
            if grid[i][j] == '0':
                return
            grid[i][j] = '0' 
            if j > 0:
                bfs(i, j - 1)
            if j < m - 1:
                bfs(i, j + 1)
            if i > 0:
                bfs(i - 1, j)
            if i < n - 1:
                bfs(i + 1, j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1 
                    bfs(i, j)

        return ans