class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            if grid[i][j]==1:
                return True
            grid[i][j]=1
            up=dfs(i-1,j)
            down=dfs(i+1,j)
            left=dfs(i,j-1)
            right=dfs(i,j+1)
            return up and down and left and right
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    if dfs(i,j):
                        count+=1
        return count