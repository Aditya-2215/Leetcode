class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if matrix is None:
            return 0
        dir=[[-1,0],[0,1],[1,0],[0,-1]]
        n=len(matrix)
        m=len(matrix[0])
        memo={}
        def agent(i,j,prev):
            if i<0 or j<0 or i>=n or j>=m or matrix[i][j]<=prev:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            curr=matrix[i][j]
            max_len=0
            for dx,dy in dir:
                max_len=max(max_len,agent(i+dx,j+dy,curr))
            memo[(i,j)]=1+max_len
            return memo[(i,j)]
        ans = 0

        for i in range(n):
            for j in range(m):
                ans = max(ans, agent(i, j, float('-inf')))

        return ans