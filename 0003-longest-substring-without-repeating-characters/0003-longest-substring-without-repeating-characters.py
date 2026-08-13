class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        hasht = {}
        
        # Using a for-loop automatically increments 'right' and avoids infinite loops
        for right in range(len(s)):
            ch = s[right]
            
            # If the character is in the map and within the current window boundaries
            if ch in hasht and hasht[ch] >= left:
                left = hasht[ch] + 1
            
            # Record or update the latest index of the character
            hasht[ch] = right
            
            # Calculate the current window size and maximize
            max_len = max(max_len, right - left + 1)
            
        return max_len
