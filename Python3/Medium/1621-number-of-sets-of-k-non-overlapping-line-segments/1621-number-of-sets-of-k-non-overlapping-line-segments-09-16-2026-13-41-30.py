class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        sumMemo = {}
        def solve(start, k):
            if k == 0:
                return 1
            if start >= n:
                return 0
            if (start, k) in memo:
                return memo[(start, k)]
            ans = solve(start + 1, k)
            ans += sumWays(start + 1, k - 1)
            memo[(start, k)] = ans % MOD
            return memo[(start, k)]
        def sumWays(start, k):
            if start >= n:
                return 0
            if (start, k) in sumMemo:
                return sumMemo[(start, k)]


            ans = solve(start, k) + sumWays(start + 1, k)

            sumMemo[(start, k)] = ans % MOD

            return sumMemo[(start, k)]

        return solve(0, k)