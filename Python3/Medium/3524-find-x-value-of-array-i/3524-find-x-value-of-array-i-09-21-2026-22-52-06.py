class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        memo = {}
        def solve(i, m):
            if i == n:
                return
            m = tuple(m)
            if (i, m) in memo:
                return memo[(i, m)]
            temp = [0] * k
            r = nums[i] % k
            temp[r] += 1
            j = 0
            while j < k:
                nr = (j * r) % k
                temp[nr] += m[j]
                j += 1
            j = 0
            while j < k:
                ans[j] += temp[j]
                j += 1
            memo[(i, m)] = True
            solve(i + 1, temp)
        ans = [0] * k
        solve(0, [0] * k)
        return ans