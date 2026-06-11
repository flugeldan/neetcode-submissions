class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        n,m=len(nums1),len(nums2)
        total=n+m
        left, right=0,n
        while left<=right:
            i=(left+right)//2
            j=((m+n+1)//2)-i

            ALeft=float('-inf') if i==0 else nums1[i-1]
            ARight= float('inf') if i == len(nums1) else nums1[i]
            BLeft=float('-inf') if j==0 else nums2[j-1]
            BRight=float('inf') if j==len(nums2) else nums2[j]

            if min(ARight, BRight) >= max(ALeft,BLeft):
                if total%2==0:
                    return (min(BRight,ARight)+max(ALeft,BLeft))/2
                else:
                    return max(BLeft,ALeft)
            if ALeft > BRight:
                right=i-1
            elif ARight < BLeft:
                left=i+1         