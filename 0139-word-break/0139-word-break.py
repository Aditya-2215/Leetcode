class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)
        memo={}
        def solve(i):
            if i==len(s):
                return True
            if i in memo:
                return memo[i]
            
            for j in range(i+1,len(s)+1):
                if s[i:j] in wordSet:
                    if solve(j):
                        memo[i]=True
                        return True
            memo[i]=False
            return False
        return solve(0)