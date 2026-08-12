class Solution:
    def maxSubarrayLength(self, nums, k):
        # Intuition: window size never shrinks, only slides; track how many values exceed k
        n = len(nums)
        left = 0
        bad = 0
        freq = {}
        for right in range(n):
            c = nums[right]
            cnt = freq.get(c, 0) + 1
            freq[c] = cnt
            if cnt == k + 1:
                bad += 1
            if bad == 0:
                continue
            d = nums[left]
            dc = freq[d] - 1
            freq[d] = dc
            if dc == k:
                bad -= 1
            left += 1
        return n - left