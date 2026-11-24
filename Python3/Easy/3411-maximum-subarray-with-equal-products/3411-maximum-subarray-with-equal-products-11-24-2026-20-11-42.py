from functools import reduce
import math
class Solution:
  def maxLength(self, nums: list[int]) -> int:
    n = len(nums)
    best = 0
    for i in range(n):
      prod = 1
      curr_gcd = 0
      curr_lcm = 1
      for j in range(i, n):
        val = nums[j]
        prod *= val
        curr_gcd = val if curr_gcd == 0 else math.gcd(curr_gcd, val)
        curr_lcm = math.lcm(curr_lcm, val)
        if prod == curr_lcm * curr_gcd:
          best = max(best, j - i + 1)
    return best