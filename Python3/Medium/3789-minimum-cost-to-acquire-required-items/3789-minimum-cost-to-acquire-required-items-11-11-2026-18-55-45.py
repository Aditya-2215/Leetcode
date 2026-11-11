class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        both = min(need1, need2)
        cost = both * min(costBoth, cost1 + cost2)
        need1 -= both
        need2 -= both
        cost += need1 * min(cost1, costBoth)
        cost += need2 * min(cost2, costBoth)

        return cost