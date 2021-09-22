def solution(n, computers):

    def _dfs(curr):

        # marking
        visited[curr] = True

        # visit next node
        for next in range(n):
            if computers[curr][next] and not visited[next]:
                _dfs(next)
        return

    visited = [False] * n
    cnt_networks = 0

    for computer in range(n):
        if not visited[computer]:
            cnt_networks += 1
            _dfs(computer)

    return cnt_networks

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
