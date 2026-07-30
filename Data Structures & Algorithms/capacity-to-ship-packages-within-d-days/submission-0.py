class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = 0
        while l < r:
            mid = (l + r) // 2
            need = 0
            cur_sum = 0
            for weight in weights:
                cur_sum += weight
                if cur_sum > mid:
                    need += 1 
                    cur_sum = weight
                elif cur_sum == mid:
                    need += 1 
                    cur_sum = 0 
            
            if cur_sum > 0:
                need += 1 
            if need <= days:
                r = mid
            else:
                l = mid + 1
        return r


        