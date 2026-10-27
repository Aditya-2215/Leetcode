class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        memo = {}

        def solve(i, j):
            if i == 0:
                return j

            if j == 0:
                return i

            if (i, j) in memo:
                return memo[(i, j)]

            if str1[i - 1] == str2[j - 1]:
                res = 1 + solve(i - 1, j - 1)

            else:
                left = 1 + solve(i - 1, j)
                right = 1 + solve(i, j - 1)

                res = min(left, right)

            memo[(i, j)] = res
            return res

        solve(n, m)

        # Reconstruct the SCS using memoized lengths
        ans = []
        i = n
        j = m

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans.append(str1[i - 1])
                i -= 1
                j -= 1

            elif solve(i - 1, j) < solve(i, j - 1):
                ans.append(str1[i - 1])
                i -= 1

            else:
                ans.append(str2[j - 1])
                j -= 1

        while i > 0:
            ans.append(str1[i - 1])
            i -= 1

        while j > 0:
            ans.append(str2[j - 1])
            j -= 1

        return "".join(ans[::-1])