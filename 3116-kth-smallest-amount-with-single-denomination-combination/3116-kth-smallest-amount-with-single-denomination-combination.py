class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def check(m):
            total=0
            for x in range(1,len(coins)+1):
                for c in combinations(coins,x):
                    total+=m//lcm(*c)*pow(-1,x+1)
            return total>=k
        return bisect_left(range(k*coins[0]+1),True,lo=1,key=check)