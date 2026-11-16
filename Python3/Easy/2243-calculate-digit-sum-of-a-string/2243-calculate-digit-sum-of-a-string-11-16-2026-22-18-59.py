class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new=""
            for i in range(0,len(s),k):
                total=0
                for j in s[i:i+k]:
                    total+=int(j)
                new+=str(total)
            s=new
        return s