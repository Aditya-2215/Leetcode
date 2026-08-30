class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        min_I=nums.index(min(nums))
        max_I=nums.index(max(nums))
        left=min(min_I,max_I)
        right=max(min_I,max_I)
        front=right+1
        back=n-left
        frontback=(left+1)+(n-right)
        return min(front,back,frontback)