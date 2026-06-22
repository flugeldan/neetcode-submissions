class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [None]
        for val in nums:
            self.add_without_returning(val)
    
    def pop(self):
        
        while len(self.nums) > self.k + 1:
            self.nums[1] = self.nums.pop()
            i = 1
            
            while i * 2 <= len(self.nums) - 1:
                left = i * 2
                right = i * 2 + 1
                if right < len(self.nums):
                    minChild = None
                    if self.nums[left] <= self.nums[right]:
                        minChild = left
                    else:
                        minChild = right
                    if self.nums[i] > self.nums[minChild]:
                        self.nums[i], self.nums[minChild] = self.nums[minChild], self.nums[i]
                        i = minChild
                    else:
                        break
                    
                elif left < len(self.nums):
                    if self.nums[left] < self.nums[i]:
                        self.nums[i], self.nums[left] = self.nums[left], self.nums[i]
                        i = left
                    else:
                        break
                else:
                    break
                    



    
    def add_without_returning(self, val):
        self.nums.append(val)
        cur = len(self.nums) - 1
        while cur > 1 and self.nums[cur] < self.nums[cur // 2]:
            self.nums[cur], self.nums[cur // 2] = self.nums[cur // 2], self.nums[cur]
            cur = cur // 2
        self.pop()
        
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        cur = len(self.nums) - 1
        while cur > 1 and self.nums[cur] < self.nums[cur // 2]:
            self.nums[cur], self.nums[cur // 2] = self.nums[cur // 2], self.nums[cur]
            cur = cur // 2 
        self.pop()
        return self.nums[1]




        
