class Solution:
    def nodesBetweenCriticalPoints(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        criticalPoints = []
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                criticalPoints.append(i)
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                criticalPoints.append(i)
        m = len(criticalPoints)
        if m < 2:
            return [-1, -1]
        minDist = float('inf')
        maxDist = criticalPoints[m - 1] - criticalPoints[0]
        for i in range(1, m):
            minDist = min(
                minDist,
                criticalPoints[i] - criticalPoints[i - 1]
            )
        return [minDist, maxDist]