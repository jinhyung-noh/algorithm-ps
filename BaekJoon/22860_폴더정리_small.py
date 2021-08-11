import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

file_tree = defaultdict(lambda:[[], []]) # 0: files, 1: folders

N, M = list(map(int, sys.stdin.readline().split()))
for _ in range(N+M):
    file = list(sys.stdin.readline().split())
    file_tree[file[0]][int(file[2])].append(file[1])

Q = int(sys.stdin.readline())
queries = [None] * Q
for i in range(Q):
    queries[i] = sys.stdin.readline().strip()


def num_files(file_tree, query):

    def _dfs(current_folder):
        # add file
        for file in file_tree[current_folder][0]:
            files.append(file)
        # search next folder
        for next_folder in file_tree[current_folder][1]:
            _dfs(next_folder)

    start_folder = query.split('/')[-1]
    files = []
    _dfs(start_folder)

    return len(set(files)), len(files)

for query in queries:
    print(*num_files(file_tree, query))