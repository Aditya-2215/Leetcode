class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        
        def solve(index, buy, tran):
            # Base Case
            if index == n or tran == 0:
                return 0
                
            key = (index, buy, tran)
            if key in memo:
                return memo[key]
            
            if buy:
                buys = -prices[index] + solve(index + 1, False, tran)
                skip = solve(index + 1, True, tran)
                memo[key] = max(buys, skip)
            else:
                sell = prices[index] + solve(index + 1, True, tran - 1)
                skip = solve(index + 1, False, tran)
                memo[key] = max(sell, skip)
                
            return memo[key]
            
        # Driver Code
        return solve(0, True, 2)
