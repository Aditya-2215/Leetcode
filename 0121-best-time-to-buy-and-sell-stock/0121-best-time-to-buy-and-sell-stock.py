class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        memo={}
        def solve(index,buy,tran):
            #Base Case
            if index==n or tran==0:
                return 0
            if (index,buy,tran) in memo:
                return memo[(index,buy,tran)]
            if buy:
                buyStock=-prices[index]+solve(index+1,False,tran)
                skip=solve(index+1,True,tran)
                ans=max(buyStock,skip)
            else:
                sellStock=prices[index]+solve(index+1,True,tran-1)
                skip=solve(index+1,False,tran)
                ans=max(sellStock,skip)
            memo[(index,buy,tran)]=ans
            return ans
        return solve(0,True,1)
