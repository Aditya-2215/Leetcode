class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        max_num=max(nums) 
        memo={}
        def solve(i):
            if i>max_num:
                return 0
            if i in memo:
                return memo[i]
            skip=solve(i+1)
            take=i*count[i]+solve(i+2)
            memo[i]= max(skip,take)
            return memo[i]
        return solve(0)
        
    

