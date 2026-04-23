class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        nodes = {i:[] for i in range(n)}
        for x,y in edges:
            nodes[x].append(y)
            nodes[y].append(x)
        
        def traversal(node):
            visit.add(node)
            if len(nodes[node]) == 0:
                return
            for ele in nodes[node]:
                if ele not in visit:
                    traversal(ele)
        res = 0
        for i in range(n):
            if i not in visit:
                res+=1
                traversal(i)
        return res