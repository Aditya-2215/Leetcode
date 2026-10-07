class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = {s}
        while not (
            answers := [
                t
                for t in level
                if t.count("(") == t.count(")")
                and min(accumulate((c == "(") - (c == ")") for c in t), default=0) >= 0
            ]
        ):
            level = {
                t[:i] + t[i + 1 :] for t in level for i, c in enumerate(t) if c in "()"
            }
        return answers