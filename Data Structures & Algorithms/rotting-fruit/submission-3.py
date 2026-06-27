from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, visited = deque(), set()
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minutes = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row, col))
        
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                
                for move in moves:
                    new_row, new_col = row + move[0], col + move[1]
                    new_pos = (new_row, new_col)
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and new_pos not in visited:
                        visited.add(new_pos)
                        q.append(new_pos)
                        grid[new_row][new_col] = 2
            if q:
                minutes += 1
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return minutes



                
                



            


        