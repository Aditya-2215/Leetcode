class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        ans,pre=-1,nums[0]
        for i in range(1,n):
            if nums[i]>pre:
                ans=max(ans,nums[i]-pre)
            else:
                pre=nums[i]
        return ans