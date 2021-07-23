class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        import collections
        import heapq

        # graph
        graph = collections.defaultdict(list)
        for u, v, w in times:       # start, stop, time
            graph[u].append((v, w))
        
        # min-heapQ
        Q = [(0, k)]    # start point (time, node)

        # distance hash
        dist = collections.defaultdict(int)

        # Dijkstra search
        while Q:
            time, node = heapq.heappop(Q)   # minimum time node
            if node not in dist:
                dist[node] = time
                for next_node, next_time in graph[node]:       # add adjacent node to heapQ
                    heapq.heappush(Q, (time+next_time, next_node))
        
        # check all nodes
        if len(dist) == n:
            return max(dist.values())
        return -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))
