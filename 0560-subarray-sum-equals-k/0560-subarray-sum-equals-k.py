class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum=0
        count=0
        freq={0:1}
        for num in nums:
            pref_sum+=num
            if pref_sum-k in freq:
                count+=freq[pref_sum-k]
            freq[pref_sum]=freq.get(pref_sum,0)+1
        return count