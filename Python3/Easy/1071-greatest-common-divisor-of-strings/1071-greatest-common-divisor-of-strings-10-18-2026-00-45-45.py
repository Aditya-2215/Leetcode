class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        limit=min(len(str1),len(str2))
        for length in range(limit,0,-1):
            candidate=str1[:length]
            if len(str1)%length!=0:
                continue
            if len(str2)%length!=0:
                continue
            if candidate*(len(str1)//length)==str1 and candidate*(len(str2)//length)==str2:
                return candidate
        return ""