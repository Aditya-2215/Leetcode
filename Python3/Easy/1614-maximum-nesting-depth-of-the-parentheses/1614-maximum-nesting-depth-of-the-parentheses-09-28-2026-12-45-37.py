class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        stack=[]
        for ch in s:
            if ch=='(':
                stack.append(ch)
                res=max(res,len(stack))
            elif ch==')':
                stack.pop()
        return res