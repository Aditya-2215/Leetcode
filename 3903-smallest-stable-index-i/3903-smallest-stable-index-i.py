class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            left=max(nums[:i+1])
            right=min(nums[i:])
            if left-right<=k:
                return i
        return -1
