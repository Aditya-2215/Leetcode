class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        result=[]
        path=[]
        def backtrack(start,current_sum):
            if current_sum==target:
                result.append(path.copy())
                return
            if current_sum>target:
                return
            for i in range(start,n):
                path.append(candidates[i])
                backtrack(i,current_sum+candidates[i])
                path.pop()
        backtrack(0,0)
        return result