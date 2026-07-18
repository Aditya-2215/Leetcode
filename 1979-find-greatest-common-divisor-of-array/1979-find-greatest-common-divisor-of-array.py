class Solution:
    def findGCD(self, nums: List[int]) -> int:
        res=math.gcd(min(nums),max(nums))
        return res