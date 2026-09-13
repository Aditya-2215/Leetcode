class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        for dx in range(-(n - 1), n):
            for dy in range(-(n - 1), n):

                overlap = 0

                for i in range(n):
                    for j in range(n):

                        if img1[i][j] == 1:

                            ni = i + dx
                            nj = j + dy

                            if 0 <= ni < n and 0 <= nj < n:
                                if img2[ni][nj] == 1:
                                    overlap += 1

                ans = max(ans, overlap)

        return ans