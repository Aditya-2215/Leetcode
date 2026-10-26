
class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def solve(n):
            if n <= 1:
                return n

            if n in memo:
                return memo[n]

            memo[n] = solve(n - 1) + solve(n - 2)
            return memo[n]

        return solve(n)
