class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for ch in s:
            if ch=='(':
                stack.append(0)
            else:
                inside=stack.pop()
                score=max(2*inside,1)
                stack[-1]+=score
        return stack[0]