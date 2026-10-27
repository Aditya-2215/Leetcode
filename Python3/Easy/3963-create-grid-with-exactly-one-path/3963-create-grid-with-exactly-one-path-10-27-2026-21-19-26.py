class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[]
        def grid(i):
            if i==m:
                return []
            row_chars=[]
            for j in range(n):
                if i==0 or j==n-1:
                    row_chars.append('.')
                else:
                    row_chars.append('#')
            current="".join(row_chars)
            return [current]+grid(i+1)
        return grid(0)