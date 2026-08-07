class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]):
        n = len(grid)
        m = len(grid[0])
        memo={}
        def solve(i, j):
            if i < 0 or j < 0:
                return 0
            if grid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            up = solve(i - 1, j)
            left = solve(i, j - 1)
            memo[(i,j)]=up + left
            return memo[(i,j)]
        return solve(n - 1, m - 1)