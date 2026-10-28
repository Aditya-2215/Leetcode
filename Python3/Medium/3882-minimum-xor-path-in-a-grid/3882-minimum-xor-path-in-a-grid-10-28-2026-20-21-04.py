class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        V = 1024
        dp = [[False] * V for _ in range(n)]
        for i in range(m):
            for j in range(n):
                g = grid[i][j]
                nxt = [False] * V
                if i == 0 and j == 0:
                    nxt[g] = True
                else:
                    up = dp[j]
                    left = dp[j - 1] if j > 0 else None
                    for x in range(V):
                        if up[x] or (left is not None and left[x]):
                            nxt[x ^ g] = True
                dp[j] = nxt
        for x in range(V):
            if dp[n - 1][x]:
                return x
        return -1