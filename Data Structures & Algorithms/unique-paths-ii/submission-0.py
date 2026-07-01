class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        memo = {}
        def smartDFS(row, col):
            if row >= len(obstacleGrid) or col >= len(obstacleGrid[0]) or obstacleGrid[row][col] == 1:
                return 0 
            if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            memo[(row, col)] = smartDFS(row + 1, col) + smartDFS(row, col + 1)
            return memo[(row, col)]
        return smartDFS(0,0)            
        