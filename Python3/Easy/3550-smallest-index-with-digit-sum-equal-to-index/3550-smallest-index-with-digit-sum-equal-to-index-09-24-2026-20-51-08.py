class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            m=nums[i]
            s=0
            while m>0:
                s+=m%10
                m//=10
            if s==i:
                return i
        return -1