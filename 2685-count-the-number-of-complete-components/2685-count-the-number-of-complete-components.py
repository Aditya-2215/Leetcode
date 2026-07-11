class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[]
        for i in range(n):
            graph.append([])
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*n
        ans=0

        def dfs(node):
            visited[node]=True
            component.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        for i in range(n):
            if not visited[i]:
                component=[]
                dfs(i)
                edge_count=0
                for node in component:
                    edge_count+=len(graph[node])
                edge_count//=2
                vertices=len(component)
                if edge_count==vertices*(vertices-1)//2:
                    ans+=1
        return ans