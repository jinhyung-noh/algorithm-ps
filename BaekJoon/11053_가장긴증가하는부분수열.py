import sys

def longest_partial_sequence():

    def _inner(start_idx: int, curr_idx: int):

        for next_idx in range(curr_idx + 1, N):

            # proceed if next is bigger than current
            if arr[next_idx] > arr[curr_idx]:
                visited[start_idx] = max(visited[start_idx], visited[next_idx] + 1)

    # input
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    visited = [1] * (N)

    # start searching in reverse order
    for start_idx in range(N-1, -1, -1):
        _inner(start_idx, start_idx)

    maximum_length = max(visited)
    return maximum_length

print(longest_partial_sequence())