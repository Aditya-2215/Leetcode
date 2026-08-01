class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        #memo={}
        @cache
        def solve(index,buy,tran):
            #Base Case
            if index==n:
                return 0
            if tran==0:
                return 0
           # key=(index,buy,tran)
           # if key in memo:
           #     return memo[key]
            #if person buys the stock and Not Buy it then we use here buys and skip respectively 
            if buy:
                buys=-prices[index]+solve(index+1,False,tran)
                skip=solve(index+1,True,tran)
                return max(buys,skip)
              #  memo[key]=max(buys,skip)
                # return memo[key]
            #For buying the second stock we need to first sell the previous stock
            else:
                sell=prices[index]+solve(index+1,True,tran-1)
                skip=solve(index+1,False,tran)
                return max(sell,skip)
                # memo[key]=max(sell,skip)
                # return memo[key]
        #Driver Code
        return solve(0,True,2)
