class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=arr[:]
        temp.sort()
        rank={}
        current_rank=1
        for num in temp:
            if num not in rank:
                rank[num]=current_rank
                current_rank+=1
        for i in range(len(arr)):
            arr[i]=rank[arr[i]]
        return arr
        