import sys

def max_height():

    def _woods(k: int):
        """return amount of woods when k height"""
        sum = 0
        for tree in trees:
            if tree > k:
                sum += tree - k
        return sum

    def _binary_search(left: int, right: int):

        while left <= right:
            center = (left + right) // 2
            woods = _woods(center)

            if woods == target:
                return center

            elif woods > target:
                left = center + 1
            else:
                right = center - 1

        return right

    # inputs
    n, target = list(map(int, sys.stdin.readline().split()))
    trees = list(map(int, sys.stdin.readline().split()))

    max_tree = max(trees)

    return _binary_search(0, max_tree)

print(max_height())



