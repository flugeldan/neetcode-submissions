class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        
        def smartDFS(row, col):
            nonlocal memo
            if row == m or col == n:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            if row == m - 1 and col == n - 1:
                return 1
            memo[(row, col)] = smartDFS(row + 1, col) + smartDFS(row, col + 1) 
            return memo[(row, col)]
        return smartDFS(0, 0)