class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        lastrow=matrix[len(matrix)-1]
        lastind=len(lastrow)-1

        if matrix[0][0] <= target <= lastrow[len(lastrow)-1]:
            bottom=0
            top=len(matrix)-1
            while bottom <= top:
                mid=(top+bottom)//2
                if target >= matrix[mid][0] and  target <=matrix[mid][lastind]:
                    left=0
                    right=len(matrix[mid])-1
                    while left<= right:
                        num=(right+left)//2
                        if matrix[mid][num] == target:
                            return True
                        elif target > matrix[mid][num]:
                            left=num+1
                        elif target < matrix[mid][num]:
                            right=num-1
                    return False
                elif target > matrix[mid][0] and target >matrix[mid][lastind]:
                    bottom=mid+1
                elif target < matrix[mid][0] and target < matrix[mid][lastind]:
                    top=mid-1
        
        return False
        