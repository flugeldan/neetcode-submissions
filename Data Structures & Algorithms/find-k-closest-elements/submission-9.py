
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:
            return arr
        elif abs(arr[0] - x) < abs(arr[1] - x):
            return arr[:k]
        l, j = 0, len(arr) - 1
        p1, p2 = l, j
        diff = float('inf')
        for i in range(len(arr)):
            if i - l + 1 == k:

                if i+ 1 < len(arr) and abs(arr[i + 1] - x) < abs(arr[l] - x):
                    p1, p2 = l, i
                    l += 1
                elif i + 1 < len(arr) and arr[i + 1] == arr[l] and abs(arr[i + 1] - x) == abs(arr[l] - x):
                    l += 1

                else:
                    return arr[l: i + 1]
        return arr[p1: p2 + 1]
    
       


        

        