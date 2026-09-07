class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # dp[i] stores the count of distinct subsequences ending with character chr(i + 97)
        dp = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # Calculate new subsequences: 
            # Current total + 1 (the character itself) - existing subsequences ending with char
            new_subsequences = (sum(dp) + 1 - dp[idx]) % MOD
            dp[idx] = (dp[idx] + new_subsequences) % MOD
            
        return sum(dp) % MOD