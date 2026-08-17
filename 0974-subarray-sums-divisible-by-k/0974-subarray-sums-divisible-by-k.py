class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        freq = {0: 1}
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in freq:
                count += freq[remainder]
            freq[remainder] = freq.get(remainder, 0) + 1
        return count