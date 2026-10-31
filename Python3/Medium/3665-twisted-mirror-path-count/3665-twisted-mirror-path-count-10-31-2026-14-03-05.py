
from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        memo = [[-1] * n for _ in range(m)]
        def solve(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            res = (
                walk(i, j + 1, 0) +
                walk(i + 1, j, 1)
            ) % MOD

            memo[i][j] = res
            return res

        def walk(i, j, direction):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if grid[i][j] == 0:
                return solve(i, j)

            if direction == 0:
                return walk(i + 1, j, 1)

            return walk(i, j + 1, 0)

        return solve(0, 0)
