class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        merged=nums1+nums2
        k=len(merged)
        merged.sort()
        if k%2==1:
            return merged[k//2]
        return (merged[k//2]+merged[k//2-1])/2

