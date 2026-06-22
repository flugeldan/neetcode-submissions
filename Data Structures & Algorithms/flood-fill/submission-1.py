class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        origColor = image[sr][sc]
        been = set()

        def helper(i, j):
            nonlocal color
            nonlocal origColor
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
                return
            if image[i][j] == color or image[i][j] != origColor:
                return
            
            if image[i][j] == origColor:
                image[i][j] = color
            helper(i, j + 1)
            helper(i, j - 1)
            helper(i - 1, j)
            helper(i + 1, j)
        helper(sr, sc)
            
        return image


   


        