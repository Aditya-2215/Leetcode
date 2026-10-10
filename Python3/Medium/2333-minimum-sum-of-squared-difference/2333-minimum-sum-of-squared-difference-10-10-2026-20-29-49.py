class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        m = max(diff)
        k = k1 + k2
        bucket = [0] * (m + 1)

        for x in diff:
            bucket[x] += 1

        for i in range(m, 0, -1):
            take = min(bucket[i], k)
            bucket[i] -= take
            bucket[i - 1] += take
            k -= take
            if k == 0:
                break

        return sum(i * i * bucket[i] for i in range(1, m + 1))