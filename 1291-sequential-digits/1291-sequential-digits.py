class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        for i in range(1,10):
            num=i
            for j in range(i+1,10):
                num=num*10+j
                if low<=num<=high:
                    ans.append(num)
        ans.sort()
        return ans