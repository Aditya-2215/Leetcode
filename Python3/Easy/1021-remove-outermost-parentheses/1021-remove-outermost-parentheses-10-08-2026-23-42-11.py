class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[0]
        ans=""
        for ch in s:
            if ch=='(':
                if len(stack)>1:
                    ans+=ch
                stack.append(1)
            else:
                stack.pop()
                if len(stack)>1:
                    ans+=ch
        return ans