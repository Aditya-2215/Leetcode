class Solution:
    def reverse(self, x: int) -> int:
        # Initialize result (reversed number)
        rev = 0

        # Check if number is negative
        sign = -1 if x < 0 else 1

        # Work with positive version of x to simplify logic
        x = abs(x)

        # Loop until x becomes 0
        while x != 0:
            # Step 1: Get the last digit of x
            digit = x % 10     # Example: 123 % 10 = 3

            # Step 2: Remove the last digit from x
            x //= 10           # Example: 123 // 10 = 12

            # Step 3: Check for overflow BEFORE pushing digit
            # 32-bit signed integer range: [-2^31, 2^31 - 1]
            if rev > (2**31 - 1) // 10:
                # If multiplying by 10 will overflow, return 0
                return 0

            # Step 4: Append the digit to the reversed number
            rev = rev * 10 + digit
            # Example: rev = 32 * 10 + 1 → 321

        # Step 5: Reapply the original sign
        rev *= sign

        # Step 6: Final overflow check
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        # Step 7: Return the reversed integer
        return rev
