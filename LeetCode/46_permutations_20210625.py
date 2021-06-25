class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def _permute_helper(num_list, path=[]):
            # when finish search
            if len(path) == len(nums):
                result.append(path)
                return None

            for num in num_list:
                _permute_helper([elem for elem in num_list if elem != num], path+[num]) 

        result = []
        _permute_helper(nums)
        return result

# solution in Book
class Solution2:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # leaf node --> append
            if len(elements) == 0:
                results.append(prev_elements[:])

            # recursion
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return results
        

# solution using itertool module
class Solution3:
    def permute(self, nums: list[int]) -> list[list[int]]:
        import itertools
        return list(map(list, itertools.permutations(nums)))
        
nums = [0,1,2]
print(Solution3().permute(nums))