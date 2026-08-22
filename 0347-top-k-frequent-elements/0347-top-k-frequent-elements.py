class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        sorted_freq=sorted(freq,key=freq.get,reverse=True)
        return sorted_freq[:k]