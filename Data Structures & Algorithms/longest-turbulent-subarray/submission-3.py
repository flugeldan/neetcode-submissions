class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1 
        maxWindow = 1
        prev = None
        l = 0
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                cur = '>'
            elif arr[i - 1] < arr[i]:
                cur = '<'
            else:
                cur = '='
            if cur == '=':
                l = i
            elif cur == prev:
                l = i - 1
            maxWindow = max(maxWindow, i - l + 1)
                
            prev = cur

                
            
        return maxWindow


        