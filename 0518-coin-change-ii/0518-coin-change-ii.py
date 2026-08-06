class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        memo={}
        def solve(i,amount):
            if amount==0:
                return 1
            if i==n or amount<0:
                return 0
            if (i,amount) in memo:
                return memo[(i,amount)]
            take=0
            if coins[i]<=amount:
                take=solve(i,amount-coins[i])
            not_take=solve(i+1,amount)
            ans=take+not_take
            memo[(i,amount)]=ans
            return ans
        return solve(0,amount)