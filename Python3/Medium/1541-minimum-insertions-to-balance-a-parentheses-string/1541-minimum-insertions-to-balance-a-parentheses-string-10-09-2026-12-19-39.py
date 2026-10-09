class Solution:
    def minInsertions(self, s: str) -> int:
        count=0
        ans=0
        for ch in s:
            if ch=="(":
                count+=2

                if count%2==1:
                    ans+=1
                    count-=1
            else:
                count-=1
                if count<0:
                    ans+=1
                    count=1
        return ans+count