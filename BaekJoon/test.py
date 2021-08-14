import sys

def longest_partial_sequence():

    def _dfs(start_idx: int, curr_idx: int):

        # recursive call
        for next_idx in range(curr_idx + 1, N):

            # proceed if next is bigger than current
            if arr[next_idx] > arr[curr_idx]:

                visited[start_idx] = max(visited[start_idx], visited[next_idx] + 1)
                return 

            # terminate condition
            if next_idx == N-1:
                visited[start_idx] = 1
                return
    # input
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    visited = [0] * (N-1) + [1]

    # start searching in reverse order 5
    for start_idx in range(N-1, -1, -1):
        _dfs(start_idx, start_idx)

    maximum_length = max(visited)
    return maximum_length

print(longest_partial_sequence())