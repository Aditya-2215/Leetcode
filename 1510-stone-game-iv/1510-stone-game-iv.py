class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo={}
        def solve(n):
            if n == 0:
                return False
            if n in memo:
                return memo[n]

            i = 1
            while i * i <= n:
                if not solve(n - i * i):
                    memo[n]=True
                    return True
                i += 1
            memo[n]=False
            return False

        return solve(n)