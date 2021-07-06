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

# solution in book
class Solution2:
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