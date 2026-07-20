class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = {}
        def LCS(i, j):
            if i == n or j == m:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + LCS(i + 1, j + 1)
            else:
                memo[(i, j)] = max(LCS(i + 1, j), LCS(i, j + 1))
                
            return memo[(i, j)]
            
        return LCS(0, 0)
