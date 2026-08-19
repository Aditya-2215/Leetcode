class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        for r, c in zeros:
            for j in range(n):
                matrix[r][j] = 0
            for i in range(m):
                matrix[i][c] = 0