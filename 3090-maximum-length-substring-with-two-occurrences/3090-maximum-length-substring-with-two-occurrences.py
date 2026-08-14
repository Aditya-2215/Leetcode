class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left=0
        d={}
        max_len=0
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            while d[s[right]]>2:
                d[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len