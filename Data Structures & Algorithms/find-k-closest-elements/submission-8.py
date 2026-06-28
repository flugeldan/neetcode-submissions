from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:
            return arr
        elif abs(arr[0] - x) < abs(arr[1] - x):
            return arr[:k]
        l, j = 0, len(arr) - 1
        diff = float('inf')
        for i in range(len(arr) - 1):
            if i - l + 1 == k:
                if abs(arr[i + 1] - x) < abs(arr[l] - x) or arr[i + 1] == arr[i]:
                    l += 1 
                else:
                    j = i
                    return arr[l: i + 1]
        return arr[l: j +1]
        
       


        

        