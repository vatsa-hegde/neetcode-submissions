class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for x,y in prerequisites:
            prereq[x].append(y)
        visited, cycle = set(), set()
        res = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            
        