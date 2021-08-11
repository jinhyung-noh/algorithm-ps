import sys
sys.setrecursionlimit(1000000)

import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

file_tree = defaultdict(lambda:[[], []]) # 0: files, 1: folders

# make file_tree
N, M = list(map(int, sys.stdin.readline().split()))
for _ in range(N+M):
    file = list(sys.stdin.readline().split())
    file_tree[file[0]][int(file[2])].append(file[1])

# move query
K = int(sys.stdin.readline())
move_queries = [None] * K
for i in range(K):
    move_queries[i] = sys.stdin.readline().strip()


# query
Q = int(sys.stdin.readline())
queries = [None] * Q
for i in range(Q):
    queries[i] = sys.stdin.readline().strip()


def num_files(file_tree, query):
    """print kind and number of files of given query"""
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

def move_folder(file_tree, move_query):

    move_from, move_to = move_query.split()

    parent_move_from, move_from = move_from.split('/')[-2:]
    move_to = move_to.split('/')[-1]

    # move folders
    file_tree[move_to][1] += file_tree[move_from][1]

    # move files
    for file in file_tree[move_from][0]:
        if file not in file_tree[move_to][0]:
            file_tree[move_to][0].append(file)
    
    # delete move_from folder in file_tree
    del file_tree[move_from]

    # delete move_from from parent folder
    file_tree[parent_move_from][1].remove(move_from)


for move_query in move_queries:
    move_folder(file_tree, move_query)

for query in queries:
    print(*num_files(file_tree, query))