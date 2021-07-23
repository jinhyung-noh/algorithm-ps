class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import defaultdict

        # make graph
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # check circularity
        traced = set()

        # check visited node
        visited = set()

        # dfs_recursive inner function
        def _dfs(n):

            # check circularity
            if n in traced:
                return False
            traced.add(n)

            # recursive dfs
            for child in graph[n]:
                # check if visited child node
                # avoid overlapped searching
                if child in visited:
                    continue

                # if _dfs(child) returns False --> there is circularity
                if not _dfs(child):
                    return False
            # remove node n for searching higher node
            traced.remove(n)

            # add to visited_node
            visited.add(n)

            return True

        for x in list(graph):
            if not _dfs(x):
                return False
        return True


numCourses =  5
prerequisites = [[1,0], [0,1]]
print(Solution().canFinish(numCourses, prerequisites))




        
        
        