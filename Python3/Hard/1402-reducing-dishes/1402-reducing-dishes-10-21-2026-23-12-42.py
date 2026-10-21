class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        n=len(satisfaction)
        satisfaction.sort()
        dp=[[0]*(n+2) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for time in range(n,0,-1):
                pick=satisfaction[i]*time+dp[i+1][time+1]
                skip=dp[i+1][time]
                dp[i][time]=max(pick,skip)
        return dp[0][1]