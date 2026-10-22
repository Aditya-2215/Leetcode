class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        memo={}
        def solve(i,j):
            if i==0 or j==0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i-1]==text2[j-1]:
                memo[(i,j)]=1+solve(i-1,j-1)
            else:
                memo[(i,j)]=max(solve(i-1,j),solve(i,j-1))
            return memo[(i,j)]
        return solve(n,m)