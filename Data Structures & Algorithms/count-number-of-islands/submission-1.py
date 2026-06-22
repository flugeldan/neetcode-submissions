class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def helper(i, j):
            grid[i][j] = 0
            if i + 1 < len(grid) and grid[i + 1][j] == '1':
                helper(i + 1, j)
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                helper(i - 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
                helper(i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                helper(i, j - 1)
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    helper(row, col)
                    ans += 1 
        return ans

        







        