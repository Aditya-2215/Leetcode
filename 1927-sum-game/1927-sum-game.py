class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        
        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    left_q += 1
                else:
                    left_sum += int(num[i])
            else:
                if num[i] == '?':
                    right_q += 1
                else:
                    right_sum += int(num[i])

        if (left_q + right_q) % 2 != 0:
            return True

        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)