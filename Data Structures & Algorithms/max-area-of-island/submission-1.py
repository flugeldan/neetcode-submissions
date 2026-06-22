class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        variants = []
        maxArea = 0


        def helper(i, j):
            variants[-1] += 1 
            grid[i][j] = 0
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                helper(i + 1, j)
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                helper(i - 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                helper(i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                helper(i, j - 1)
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    variants.append(0)
                    helper(row, col)
                    maxArea = max(maxArea, variants[-1])
        return maxArea
                

            
        