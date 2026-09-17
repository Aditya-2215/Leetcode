class Solution:

    def countSquares(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        def solve(r, c):
            if r >= m or c >= n:
                return 0
            if matrix[r][c] == 0:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r, c)] = 1 + min(
                solve(r, c + 1),
                solve(r + 1, c),
                solve(r + 1, c + 1)
            )
            return memo[(r, c)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += solve(i, j)
        return ans