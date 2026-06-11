from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        maxnums = []
        for i in range(len(nums)):
            element = nums[i]
            
            while q and element >= nums[q[-1]]:
                q.pop()
            
            if q and q[0] <= i-k:
                q.popleft()
            q.append(i)
            if q and i >= k-1:
                maxnums.append(nums[q[0]])

        return maxnums

            

            
            
            


        
            
                

            
        


            





        

