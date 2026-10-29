class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            graph[v].append(u)
        visited=[0]*numCourses
        def dfs(node):    
            if visited[node]==1:
                return False
            if visited[node]==2:
                return True
            visited[node]=1
            for padoshi in graph[node]:
                if not dfs(padoshi):
                    return False
            visited[node]=2
            return True
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        return True
