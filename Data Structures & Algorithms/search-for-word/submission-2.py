class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        rows, cols = len(board), len(board[0])
        starts = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if len(word) == 1:
                        return True
                    starts.append((row, col))









        flag = False
        been, curBeen = set(), set()
        def dfs(pos, i):
            nonlocal flag
            nonlocal rows
            nonlocal cols
            nonlocal moves
            if i == len(word) - 1:
                flag = True
                return
            curBeen.add(pos)
            row, col = pos
            for move in moves:
                row_move, col_move = move
                new_row, new_col = row + row_move, col + col_move
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == word[i + 1] and (new_row, new_col) not in curBeen:
                    dfs((new_row, new_col), i + 1)
                    if flag:
                        return
            curBeen.remove(pos)
        for pos in starts:
            
            dfs(pos, 0)
            if flag:
                return True
        return False

        