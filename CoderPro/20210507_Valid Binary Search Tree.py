# time O(n)  : in case where we have to check all n nodes
# space O(n) : it depends on how many recursive step recalled, in case where all nodes are linked series; left-left-...
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Helper function which validates whether each node is valid for Binary Search Tree
    def _isValidBSTHelper(self, node, low, high):
        if not node:
            return True
        val = node.val
        if (val > low and val < high) and \
            self._isValidBSTHelper(node.left, low, val) and \
            self._isValidBSTHelper(node.right, val, high):
            return True
        return False
    def isValidBST(self, node):
        # lowerbound(-inf), upperbound(inf) for root node
        return self._isValidBSTHelper(node, float('-inf'), float('inf'))

#     5
#    / \
#   4   7
#        \
#         6

node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(6)

print(Solution().isValidBST(node))


