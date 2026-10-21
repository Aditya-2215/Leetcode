class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        n=len(satisfaction)
        satisfaction.sort()
        memo={}
        def solve(i,time):
            if i==n:
                return 0
            if (i,time) in memo:
                return memo[(i,time)]
            pick=satisfaction[i]*time+solve(i+1,time+1)
            skip=solve(i+1,time)
            memo[(i,time)]=max(pick,skip)
            return memo[(i,time)]
        return solve(0,1)