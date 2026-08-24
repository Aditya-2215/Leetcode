class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        length=len(stones)
        for pos in range(1,length):
            previous=pos-1
            stones[pos]=stones[pos]+stones[previous]
        result=stones[-1]
        for pos in range(length-2,0,-1):
            result=max(result,stones[pos]-result)
        return result