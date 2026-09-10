class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total=len(set(nums))
        n=len(nums)
        ans=0
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                if len(seen)==total:
                    ans+=1
        return ans

