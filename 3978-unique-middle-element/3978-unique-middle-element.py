class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        if n%2==0:
            return False
        mid=nums[n//2]
        count=0
        for num in nums:
            if num==mid:
                count+=1
        return count==1

            
