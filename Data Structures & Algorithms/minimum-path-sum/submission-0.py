from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def bfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return float('inf')
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[-1][-1]
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = min(grid[i][j] + bfs(i + 1, j), grid[i][j] + bfs(i, j + 1))

            return memo[(i, j)]
        return bfs(0, 0)
