class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        @cache
        def solve(amount):
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            ans=float('inf')
            for coin in coins:
                ans=min(ans,1+solve(amount-coin))
            return ans
        ans=solve(amount)
        if ans==float('inf'):
            return -1
        return ans