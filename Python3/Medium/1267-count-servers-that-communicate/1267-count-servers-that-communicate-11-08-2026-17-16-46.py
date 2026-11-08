class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row_c = [0] * len(grid)
        col_c = [0] * len(grid[0])
        servers = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    row_c[row] += 1
                    col_c[col] += 1
                    servers.append((row, col))

        c_servers = 0
        for row, col in servers:
            if row_c[row] > 1 or col_c[col] > 1:
                c_servers += 1

        return c_servers