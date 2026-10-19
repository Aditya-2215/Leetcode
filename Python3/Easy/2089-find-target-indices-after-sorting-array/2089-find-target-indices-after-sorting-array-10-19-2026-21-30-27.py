class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(0,n):
            if nums[i]==target:
                ans.append(i)
        return ans