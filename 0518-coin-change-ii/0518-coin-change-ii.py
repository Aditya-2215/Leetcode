from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def solve(i, amount):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if i == len(coins):
                return 0
            take = solve(i, amount - coins[i])
            not_take = solve(i + 1, amount)
            return take + not_take
        return solve(0, amount)