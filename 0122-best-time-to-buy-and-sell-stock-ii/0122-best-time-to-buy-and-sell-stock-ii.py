class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        memo={}
        def solve(index,buy):
            #Base Case
            if index==n:
                return 0
            #key for memoization
            key=(index,buy)
            if key in memo:
                return memo[key]

            if buy:
                buy_Stocks=-prices[index]+solve(index+1,False)
                skip=solve(index+1,True)
                memo[key]=max(buy_Stocks,skip)
                return memo[key]
            else:
                sell_Stock=prices[index]+solve(index+1,True)
                skip=solve(index+1,False)
                memo[key]=max(sell_Stock,skip)
                return memo[key]
        #Driver code
        return solve(0,True)