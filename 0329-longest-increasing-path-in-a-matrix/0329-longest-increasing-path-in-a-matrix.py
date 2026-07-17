from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        ans = 0
        def f1(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            length = 1
            # Down
            if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                length = max(length, 1 + f1(i + 1, j))

            # Up
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                length = max(length, 1 + f1(i - 1, j))

            # Right
            if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                length = max(length, 1 + f1(i, j + 1))

            # Left
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                length = max(length, 1 + f1(i, j - 1))

            dp[i][j] = length
            return length

        for i in range(m):
            for j in range(n):
                ans = max(ans, f1(i, j))

        return ans