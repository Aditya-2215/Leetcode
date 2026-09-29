class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        memo = {}
        def solve(r, c, balance):
            if balance < 0:
                return False
            if r == m - 1 and c == n - 1:
                return balance == 0
            state = (r, c, balance)
            if state in memo:
                return memo[state]
            if r + 1 < m:
                if grid[r + 1][c] == '(':
                    new_balance = balance + 1
                else:
                    new_balance = balance - 1
                if solve(r + 1, c, new_balance):
                    memo[state] = True
                    return True
            if c + 1 < n:
                if grid[r][c + 1] == '(':
                    new_balance = balance + 1
                else:
                    new_balance = balance - 1
                if solve(r, c + 1, new_balance):
                    memo[state] = True
                    return True
            memo[state] = False
            return False
        first = 1 if grid[0][0] == '(' else -1
        return solve(0, 0, first)