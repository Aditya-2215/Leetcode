from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        total = 0
        left = 0
        
        for right in range(len(nums)):
            total += nums[right]  # Expand the window
            
            while total >= target:  # Contract the window
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
                
        return 0 if res == float('inf') else res
