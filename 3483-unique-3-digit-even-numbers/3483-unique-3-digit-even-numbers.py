class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
        ans = set()
        def solve(pos, num):
            if pos == 3:
                ans.add(num)
                return
            for d in range(10):
                if freq[d] == 0:
                    continue
                if pos == 0 and d == 0:
                    continue
                if pos == 2 and d % 2 != 0:
                    continue
                freq[d] -= 1
                solve(pos + 1, num * 10 + d)
                freq[d] += 1
        solve(0, 0)
        return len(ans)