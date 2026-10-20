class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        suff = [float('inf')] * (n + 1)
        drop = [0] * n

        for i in range(n):
            pref[i + 1] = max(pref[i], nums[i])

        for i in range(n - 1, -1, -1):
            suff[i] = min(nums[i], suff[i + 1])

        for i in range(1, n):
            drop[i] = drop[i - 1] + (nums[i - 1] > nums[i])

        def check(k):
            for start in range(0, n, k):
                end = start + k - 1

                d = drop[end] - drop[start]

                if nums[end] > nums[start]:
                    d += 1

                if d > 1 or pref[start] > suff[start]:
                    return False

            return True

        ans = 0

        for k in range(1, int(n ** 0.5) + 1):
            if n % k == 0:
                if check(k):
                    ans += k

                other = n // k
                if other != k and check(other):
                    ans += other

        return ans