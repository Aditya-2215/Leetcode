class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(n - 1, -1, -1):
            for amt in range(1, amount + 1):
                take = 0
                if coins[i] <= amt:
                    take = dp[i][amt - coins[i]]
                not_take = dp[i + 1][amt]
                dp[i][amt] = take + not_take
        return dp[0][amount]