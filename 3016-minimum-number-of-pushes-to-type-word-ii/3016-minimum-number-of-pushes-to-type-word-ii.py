class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=[0]*26
        for ch in word:
            freq[ord(ch)-ord('a')]+=1
        ans=0
        assigned=0
        while True:
            maxi=0
            idx=-1
            for i in range(26):
                if freq[i]>maxi:
                    maxi=freq[i]
                    idx=i
            if idx==-1:
                break
            ans+=maxi*(assigned//8+1)
            freq[idx]=0
            assigned+=1
        return ans

