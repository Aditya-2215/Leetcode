class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]
        suffixSum = [0] * n
        suffixSum[-1] = piles[-1]

        for x in range(n - 2, - 1, - 1):
            suffixSum[x] = suffixSum[x+1] + piles[x]

        for x in range(n - 1, - 1, - 1):
            for y in range(1, n + 1):
                if x + 2 * y >= n:
                    dp[x][y] = suffixSum[x]
                else:
                    for j in range(1, 2 * y + 1):
                        dp[x][y] = max(dp[x][y], suffixSum[x] - dp[x +j][max(y, j)])
        return dp[0][1]