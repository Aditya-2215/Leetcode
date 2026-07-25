class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]
        while n:
            d=n%10
            arr.append(d)
            n//=10
        arr.sort()
        return arr[-1]*arr[-2]