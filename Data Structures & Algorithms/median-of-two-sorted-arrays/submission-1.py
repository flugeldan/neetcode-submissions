class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1
        n=len(nums1)
        m=len(nums2)
        left,right=0,n
        while left <=right:
            i=(left+right)//2
            j=((n+m+1)//2)-i

            aLeft=float('-inf') if i == 0 else nums1[i-1]
            aRight=float('inf') if i == n else nums1[i]
            bLeft=float('-inf') if j==0 else nums2[j-1]
            bRight=float('inf') if j==m else nums2[j]

            if min(aRight,bRight ) >= max(aLeft, bLeft):
                if (n+m)%2==0:
                    return (max(aLeft,bLeft)+min(aRight,bRight))/2
                else:
                    return max(aLeft,bLeft)
            if aLeft > bRight:
                right=i-1
            elif aRight < bLeft:
                left=i+1
        

        