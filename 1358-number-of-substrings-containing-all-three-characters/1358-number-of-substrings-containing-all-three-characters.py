class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        ans = 0
        n = len(s)
        mp = {}
        for j in range(n):
            mp[s[j]] = mp.get(s[j], 0) + 1

            while len(mp) == 3:
                ans += (n - j)
                mp[s[i]] -= 1
                if mp[s[i]] == 0:
                    del mp[s[i]]
                i += 1
        return ans