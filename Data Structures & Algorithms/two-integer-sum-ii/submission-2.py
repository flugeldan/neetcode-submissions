class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        hashmap={}
        while left< len(numbers):
            for j in range(left+1, len(numbers)):
                if numbers[left]+numbers[j]==target:
                    return [left+1, j+1]
            left+=1

            
        