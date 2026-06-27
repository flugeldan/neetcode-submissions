from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] == 1 or grid[0][0] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        q = deque([(0, 0)])
        visited = set((0, 0))
        depth = 0
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, 1]]
        while q:
            depth += 1 
            for i in range(len(q)):
                row, col = q.popleft()
                for move in moves:
                    row_move, col_move = move
                    new_row, new_col = row + row_move, col + col_move
                    new_pos = (new_row, new_col)
                    if new_pos == (rows - 1, cols - 1):
                        return depth + 1
                    if 0 <= new_row < rows and 0 <= new_col < cols and new_pos not in visited and grid[new_row][new_col] == 0:
                        visited.add(new_pos)
                        q.append(new_pos)
        return -1





        