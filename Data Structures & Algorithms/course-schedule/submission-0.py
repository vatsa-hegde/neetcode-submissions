class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for x, y in prerequisites:
            if x not in prereq:
                prereq[x] = []
            prereq[x].append(y)
        visit = {}

        def check(course):
            if course not in prereq:
                return True
            if course in visit and visit[course] == True:
                return False
            visit[course] = True
            for ele in prereq[course]:
                if not check(ele):
                    return False
            visit[course] = False
            return True
        
        for x,y in prerequisites:
            if not check(x):
                return False
        return True
        