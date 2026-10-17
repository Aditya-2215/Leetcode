class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total

        n = len(nums)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        destination = {num: i for i, num in enumerate(target)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            current = i
            cycle_size = 0

            while not visited[current]:
                visited[current] = True
                cycle_size += 1
                current = destination[nums[current]]

            swaps += cycle_size - 1

        return swaps