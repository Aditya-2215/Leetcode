class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        ans = []

        for i in range(len(nums) - 1):
            current = nums[i]
            nxt = nums[i + 1]

            for x in range(current + 1, nxt):
                ans.append(x)

        return ans