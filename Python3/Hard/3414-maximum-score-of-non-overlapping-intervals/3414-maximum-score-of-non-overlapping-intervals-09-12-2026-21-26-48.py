import bisect

class Solution:
    def maximumWeight(self, I: List[List[int]]) -> List[int]:
        A = sorted((l, r, w, i) for i, (l, r, w) in enumerate(I))
        S, n = [x[0] for x in A], len(A)
        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, id = A[i]
            nxt = bisect.bisect_right(S, r)
            for k in range(1, 5):
                bw, bids = dp[i + 1][k]
                pw, pids = dp[nxt][k - 1]
                tw, tids = pw + w, tuple(sorted(pids + (id,)))
                dp[i][k] = (tw, tids) if tw > bw or (tw == bw and (not bids or tids < bids)) else (bw, bids)

        return list(dp[0][4][1])