class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        running=0
        res=[]
        for num in nums:
            running+=num
            res.append(running)
        return res


            

