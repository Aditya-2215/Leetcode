class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num:
            return ""
        
        ans="9"*(sum//9)
        r=sum%9
        
        if r>0:
            ans+=str(r)
        ans+="0"*(num-len(ans))
        return str(ans)