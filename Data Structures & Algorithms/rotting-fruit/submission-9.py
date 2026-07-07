from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0
        q = deque([(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 2])
        while q:
            added = False
            for i in range(len(q)):
                cur = q.popleft()
                for move in moves:
                    new_row = move[0] + cur[0]
                    new_col = move[1] + cur[1]
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
                        added = True
            if added:
                minutes += 1 
                



        left = next((True for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 1), None)
        if left:
            return -1
        return minutes




                


        






        