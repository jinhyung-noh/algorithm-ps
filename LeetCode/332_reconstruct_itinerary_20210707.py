class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        from collections import defaultdict

        # make hash
        hash = defaultdict(list)
        for ticket in tickets:
            hash[ticket[0]].append(ticket[1])

        # sort each hash[startpoint] 
        for start_point in hash:
            hash[start_point] = sorted(hash[start_point])

        result, path = [], ["JFK"]
        pass


# solution in book
# recursive
class Solution2:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        from collections import defaultdict

        graph = defaultdict(list)
        # make graph in lexical order
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            # read first value and visit in lexical order
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        # return in reverse order
        return route[::-1]


# iterative - using stack
class Solution3:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        from collections import defaultdict

        graph = defaultdict(list)
        # make graph in lexical order
        for a, b in sorted(tickets):
            graph[a].append(b)

        stack = ["JFK"]
        route = []
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            # end of branch --> pop latest value 
            # and append to new variable "route" and continue searching 
            route.append(stack.pop())

        return route[::-1]

            
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(Solution3().findItinerary(tickets))
