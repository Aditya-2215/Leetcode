class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        memo={}
        def solve(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            ans=-float('inf')
            currSum=0
            for k in range(3):
                if i+k<n:
                    currSum+=stoneValue[i+k]
                    ans= max(ans, currSum - solve(i + k + 1))
            memo[i]=ans
            return ans
        res=solve(0)
        if res>0:
            return 'Alice'
        elif res<0:
            return 'Bob'
        else:
            return 'Tie'