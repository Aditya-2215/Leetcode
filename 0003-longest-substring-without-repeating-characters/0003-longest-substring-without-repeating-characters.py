class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        ans = 0
        for right, ch in enumerate(s):
            if ch in last:
                left = max(left, last[ch] + 1)
            last[ch] = right
            ans = max(ans, right - left + 1)
        return ans