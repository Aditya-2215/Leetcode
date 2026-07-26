class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        n=len(nums)
        a=nums[0]*nums[1]*nums[n-1]
        b=nums[n-1]*nums[n-2]*nums[n-3]
        if a>b:
            return a
        else:
            return b