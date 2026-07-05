class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxRange = -1
        ans = 0

        for num in nums:
            temp = num
            maxDigit = 0
            minDigit = 9

            while temp > 0:
                digit = temp % 10
                maxDigit = max(maxDigit, digit)
                minDigit = min(minDigit, digit)
                temp //= 10

            digitRange = maxDigit - minDigit

            if digitRange > maxRange:
                maxRange = digitRange
                ans = num
            elif digitRange == maxRange:
                ans += num

        return ans