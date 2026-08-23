class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary=""
        for ch in s:
            ascii_value=ord(ch)
            binary+=format(ascii_value,'08b')
        return binary==binary[::-1]