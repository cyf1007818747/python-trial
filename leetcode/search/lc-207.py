from typing import List

# wrong !!!
# you assumed that if only one prerequisite is taken then you can take the child
# actually, all prerequsites should be taken
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # need a childdic, a set of courses with no preprequisites, a visited list
        childdic = {}
        visited = [False] * numCourses
        courseswithoutpreq = set(list(range(numCourses)))
        for course, preq in prerequisites:
            if course in courseswithoutpreq:
                courseswithoutpreq.remove(course) 
            if preq in childdic:
                childdic[preq].append(course)
            else:
                childdic[preq] = [course]

        # do dfs starting from all courses with no prerequisites, and mark as visited
        def dfs(course: int):
            if visited[course]:
                return

            visited[course] = True
            for child in childdic.get(course, []):
                dfs(child)

        for course in courseswithoutpreq:
            dfs(course)
        
        # check whether all courses are visited
        for itm in visited:
            if not itm:
                return False

        return True
