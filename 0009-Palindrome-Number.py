class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Negative numbers or numbers ending with 0 (but not 0 itself)
        # can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0  # to store reversed half

        # Step 2: Reverse half of the digits
        while x > rev:
            digit = x % 10         # get last digit
            rev = rev * 10 + digit # build reversed half
            x //= 10               # remove last digit

        # Step 3: Check equality
        # If even number of digits → x == rev
        # If odd → ignore middle digit (rev//10)
        return x == rev or x == rev // 10
