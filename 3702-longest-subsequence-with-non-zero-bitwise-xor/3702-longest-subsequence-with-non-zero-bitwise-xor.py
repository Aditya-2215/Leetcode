class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x=0
        for num in nums:
            x^=num
        if x:
            return len(nums)
        return len(nums)-1 if any(nums) else 0