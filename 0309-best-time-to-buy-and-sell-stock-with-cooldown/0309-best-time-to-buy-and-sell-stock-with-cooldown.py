class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        #@cache #if we use this then it will automatically reduce the size of the TC from O(2^n) to O(n)
        @cache
        def solve(i,flag):
            if i>=n:
                return 0
            if flag:
                sell = +prices[i]+solve(i+2,0)
                N_sell=solve(i+1,1)
                ans=max(sell,N_sell)
                return ans
            else:
                buy=-prices[i]+solve(i+1,1)
                N_buy=solve(i+1,0)
                ans=max(buy,N_buy)
                return ans
                
        return solve(0,0)