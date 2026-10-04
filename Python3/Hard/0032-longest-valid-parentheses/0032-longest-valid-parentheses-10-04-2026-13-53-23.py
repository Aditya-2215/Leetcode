class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        res = 0

        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    res = max(res, i - st[-1])

        return res