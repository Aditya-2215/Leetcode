class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            x=n
            product=1
            while x:
                product*=x%10
                x//=10
            if product%t==0:
                return n
            n+=1