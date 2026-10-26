class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        memo={}
        def solve(i):
            if i==0:
                return cost[0]
            if i==1:
                return cost[1]
            if i in memo:
                return memo[i]
            memo[i]=cost[i]+min(solve(i-1),solve(i-2))
            return memo[i]
        return min(solve(n-1),solve(n-2))