class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def _dfs_helper(idx=0):
            # terminate condition
            if idx == len(nums):
                result.append([elem for elem in stack if elem != "" ])
                return

            # recursive call
            for elem in [nums[idx], ""]:
                stack.append(elem)
                _dfs_helper(idx+1)
                stack.pop()
            
        result = []
        stack = []
        _dfs_helper()
        return result 


class Solution2:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def _dfs_helper(idx):
            # add path everytime
            result.append(stack[:])

            # recursive dfs
            for new_idx in range(idx, len(nums)):
                stack.append(nums[new_idx])
                _dfs_helper(new_idx+1)
                stack.pop()

        result, stack = [], []
        _dfs_helper(0)
        return result
            
# solution in book
class Solution3:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(index, path):
            # add path every time
            result.append(path)

            # recursive dfs
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        result = []
        dfs(0, [])
        return result

nums = [1,2,3]
print(Solution2().subsets(nums))