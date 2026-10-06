class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened=added=0
        for ch in s:
            if ch=='(':
                opened+=1
            elif opened:
                opened-=1
            else:
                added+=1
        return opened+added
        