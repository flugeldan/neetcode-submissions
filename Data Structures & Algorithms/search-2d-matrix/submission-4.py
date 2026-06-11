class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Проверка на пустую матрицу
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                # бинпоиск по строке
                left, right = 0, cols - 1
                while left <= right:
                    num = (left + right) // 2
                    if matrix[mid][num] == target:
                        return True
                    elif matrix[mid][num] < target:
                        left = num + 1
                    else:
                        right = num - 1
                return False
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        
        return False  # ⬅️ обязательно
