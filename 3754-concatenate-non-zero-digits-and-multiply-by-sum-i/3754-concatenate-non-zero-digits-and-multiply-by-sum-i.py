class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digit_sum = 0
        ans = 0
        place = 1
        while n > 0:
            digit = n % 10
            if digit != 0:
                digit_sum += digit
                ans = digit * place + ans
                place *= 10
            n //= 10
        return ans * digit_sum