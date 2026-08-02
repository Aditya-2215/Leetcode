class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        memo={}
        def solve(i,j):
            if i==j:
                return piles[i]
            if (i,j) in memo:
                return memo[(i,j)]

            takeLeft=piles[i]-solve(i+1,j)
            takeRight=piles[j]-solve(i,j-1)
            memo[(i,j)]=max(takeLeft,takeRight)
            return memo[(i,j)]
        return solve(0,n-1)>0