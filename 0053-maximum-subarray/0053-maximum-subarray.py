class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):

            current_sum = max(nums[i], current_sum + nums[i])

            maximum = max(maximum, current_sum)

        return maximum