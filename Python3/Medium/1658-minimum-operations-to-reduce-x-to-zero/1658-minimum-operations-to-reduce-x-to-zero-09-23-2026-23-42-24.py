class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        target = sum(nums) - x

        if target < 0:
            return -1

        best = -1
        s = 0
        i = 0

        for j, num in enumerate(nums):

            s += num

            while s > target:
                s -= nums[i]
                i += 1

            if s == target:
                best = max(best, j - i + 1)

        if best == -1:
            return -1

        return len(nums) - best