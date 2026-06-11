class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #проверка строк
        for row in board:
            seen=set()
            for element in row:
                if element in seen and element!='.':
                    return False
                if element != '.':
                    seen.add(element)
        #проверка строк
        for column in range(len(board[0])):
            seen=set()
            for row in range(len(board[0])):
                if board[row][column] in seen and board[row][column] != '.':
                    return False
                if board[row][column] !='.':
                    seen.add(board[row][column])
        #проверка матриц
        for block_rows in range(0, 9, 3): #3 at the time
            for column_rows in range(0, 9, 3):
                seen=set()
                for i in range(3):
                    row=block_rows+i
                    for j in range(3):
                        column=column_rows+j
                        element=board[row][column]
                        if element in seen:
                            return False
                        if element != '.':
                            seen.add(element)
        return True                    
        