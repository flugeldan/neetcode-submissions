class Solution:
    def mySqrt(self, x: int) -> int: 
        if x <= 1:
            return x 
        l, r = 1, x
        ans = 1

        while l <= r:
            mid = (l + r) // 2
            res = mid * mid
            if res == x:
                return mid
            if res > x:
                r = mid - 1
            elif res < x:
                ans = mid
                l = mid + 1
        return ans

        