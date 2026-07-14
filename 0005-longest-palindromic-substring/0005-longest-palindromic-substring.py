class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=""
        for i in range(n):
            for j in range(i,n):
                sub=s[i:j+1]
                if sub==sub[::-1]:
                    if len(sub)>len(ans):
                        ans=sub
        return ans
