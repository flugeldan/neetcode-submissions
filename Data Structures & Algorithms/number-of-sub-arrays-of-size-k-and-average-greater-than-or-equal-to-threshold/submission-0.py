class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1 
        curProduct = 0
        ans = 0
        for i in range(r):
            curProduct += arr[i]
        for i in range(r, len(arr)):
            curProduct += arr[i]
            if curProduct / k >= threshold:
                ans += 1 
            curProduct -= arr[l]
            l += 1 
        return ans
            

        