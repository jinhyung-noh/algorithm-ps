# solution by Techlead : O(n^2), O(n)
class Solution:

    def _hasCycle(self, graph, course, seen):
        if course in seen:              # seen is a set
            return True
        if course not in graph:
            return False
        seen.add(course)
        for neighbors in graph[course]:
            if self._hasCycle(graph, neighbors, seen):
                return True
        seen.remove(course)
        return False


    def canFinish(self, numCourses, prerequisites):
        # making graph ; hashmap {courses:[prerequisites]}
        graph = {}
        for prereq in prerequisites:
            if prereq[0] in graph:                  
                graph[prereq[0]].append(prereq[1])
            else:
                graph[prereq[0]] = [prereq[1]] 
        
        for course in range(numCourses):
            if self._hasCycle(graph, course, set()):
                return False
        return True



# solution with cache : O(n), O(n)
class Solution2:

    def _hasCycle(self, graph, course, seen, cache):
        if course in cache:
            return cache[course]       # seen is a set, cache is a dict 

        if course in seen:              
            return True
        if course not in graph:
            return False

        seen.add(course)
        ret = False
        for neighbors in graph[course]:
            if self._hasCycle(graph, neighbors, seen, cache):
                ret = True
                break
        seen.remove(course)

        cache[course] = ret
        print(cache)
        return ret


    # making graph ; hashmap {courses:[prerequisites]}
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for prereq in prerequisites:
            if prereq[0] in graph:                  
                graph[prereq[0]].append(prereq[1])
            else:
                graph[prereq[0]] = [prereq[1]] 
        
        for course in range(numCourses):
            if self._hasCycle(graph, course, set(), {}):     # course마다 cache를 초기화할거면 뭐하러 cache를 만듦?? 다음꺼 활용하려고 만든거 아닌가? 
                return False
            
        return True


# cache 활용한 solution
class Solution3:
    # return a cache (dict {courses: True if it has cycle; False if not})
    def _hasCycle(self, graph, course, seen, cache):
        if course in cache:
            return cache[course]       # seen is a set, cache is a dict 

        if course in seen:              
            return True
        if course not in graph:
            return False

        seen.add(course)
        ret = False
        for neighbors in graph[course]:
            if self._hasCycle(graph, neighbors, seen, cache):
                ret = True
                break
        seen.remove(course)

        cache[course] = ret
        print(cache)
        return cache


    # making graph ; hashmap {courses:[prerequisites]}
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for prereq in prerequisites:
            if prereq[0] in graph:                  
                graph[prereq[0]].append(prereq[1])
            else:
                graph[prereq[0]] = [prereq[1]] 
        cache = {}
        for course in range(numCourses):
            if self._hasCycle(graph, course, set(), cache)[course]:     
                return False
        return True

# print(Solution().canFinish(2, [[1, 0]]))
# print(Solution().canFinish(2, [[1, 0], [0, 1]]))
print(Solution2().canFinish(4, [[1, 3], [0, 1], [0, 2], [0, 3], [2, 3]]))
print(Solution3().canFinish(4, [[1, 3], [0, 1], [0, 2], [0, 3], [2, 3]]))