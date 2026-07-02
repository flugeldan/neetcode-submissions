class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in range(len(matrix)):
            arr = [0] * (len(matrix[row]) + 1)
            for i in range(1, len(arr)):
                arr[i] = arr[i - 1] + matrix[row][i - 1]
            self.prefix.append(arr)
        

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        curSum = 0
        for row in range(row1, row2 + 1):
            curSum += self.prefix[row][col2 + 1] - self.prefix[row][col1]
        return curSum
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)