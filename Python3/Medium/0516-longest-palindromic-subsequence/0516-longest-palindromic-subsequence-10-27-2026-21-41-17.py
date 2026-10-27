class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        memo={}
        def solve(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i]==s[j]:
                res=2+solve(i+1,j-1)
            else:
                left=solve(i+1,j)
                right=solve(i,j-1)
                res=max(left,right)
            memo[(i,j)]=res
            return res
        return solve(0,n-1)
            
