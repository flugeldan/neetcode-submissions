class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in range(len(matrix)):
            row_pref = [0] * (len(matrix[0]) + 1)
            for i in range(1, len(row_pref)):
                row_pref[i] = row_pref[i - 1] + matrix[row][i - 1]
            
            if row > 0:
                for i in range(1, len(row_pref)):
                    row_pref[i] += self.prefix[row - 1][i]
            self.prefix.append(row_pref)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0:
            return self.prefix[row2][col2 + 1] - self.prefix[row2][col1]
        return (self.prefix[row2][col2 + 1] - self.prefix[row2][col1]) - (self.prefix[row1 - 1][col2 + 1] - self.prefix[row1 - 1][col1])
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)