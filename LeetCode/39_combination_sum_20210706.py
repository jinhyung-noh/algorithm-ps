class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def _dfs_helper(idx=0):
            # base case
            if sum(stack) == target:
                result.append(stack[:])
                return
            if sum(stack) >= target:
                return

            # recursive
            for new_idx in range(idx, len(candidates)):
                stack.append(candidates[new_idx])
                _dfs_helper(new_idx)
                stack.pop()
            
        result = []
        stack = []
        _dfs_helper()
        return result
        

# solution in Book
class Solution2:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(csum, index, path):
            # terminate case1: exceed target
            if csum < 0:
                return
            # terminate case2: exactily target
            if csum == 0:
                result.append(path)
                return

            # recursive call
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        result = []
        dfs(target, 0, [])
        return result




candidates = [2, 3, 5]
target = 8

print(Solution2().combinationSum(candidates, target))