class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        best = [INF] * n
        ans = INF
        prefix = 0
        last = {0: -1}
        min_len = INF
        for i in range(n):
            prefix += arr[i]
            if prefix - target in last:
                j = last[prefix - target]
                length = i - j
                if best[j] != INF:
                    ans = min(ans, length + best[j])
                min_len = min(min_len, length)
            best[i] = min_len
            last[prefix] = i
        return -1 if ans == INF else ans