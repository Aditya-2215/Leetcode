class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n=len(cost)
        INF=float('inf')
        dp=[INF]*(n+1)
        dp[0]=0
        for c,t in zip(cost,time):
            for j in range(n,0,-1):
                prev=max(0,j-t-1)
                dp[j]=min(dp[j],dp[prev]+c)
        return dp[n]