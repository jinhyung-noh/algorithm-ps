import sys

cases = []

while True:
    case = list(map(int, sys.stdin.readline().split()))
    if not case[0]:
        break
    cases.append(case)


def lotto(k: int, arr: list[int]):

    def  _print_lotto():
        for i in range(k):
            if check_list[i]:
                print(arr[i], end=" ")
        print()
        return

    def _dfs_combination(level: int, left: int):
        # base case
        if level == 6:
            return _print_lotto()

        # recursive call: dfs
        for i in range(left, k):
            if not check_list[i]:
                check_list[i] = True
                _dfs_combination(level+1, i+1)
                check_list[i] = False

    check_list = [False] * k
    for i in range(k):
        check_list[i] = True
        _dfs_combination(1, i+1)
        check_list[i] = False

for case in cases:
    lotto(case[0], case[1:])
    print()
