class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # binary search
        # return the target index[int]
        def binary_search(sorted_nums: list[tuple[int]], target: int, low: int, high: int) -> int:
            # base case:
            if low > high:
                return None
            mid = (low + high) // 2
            if sorted_nums[mid][1] == target:
                return sorted_nums[mid][0]
            elif sorted_nums[mid][1] > target:
                return binary_search(sorted_nums, target, low, mid-1)
            else:
                return binary_search(sorted_nums, target, mid+1, high)


        # we need index -> sort enumerated nums
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        for ind, num in enumerate(sorted_nums):
            target_ind =  binary_search(sorted_nums, target - num[1], ind+1, len(sorted_nums)-1)
            if target_ind is not None:
                return (num[0], target_ind)
        return None


# solution in book 
# 1 brute force : O(n^2)
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# using 'in' operater : O(n^2)
class Solution3:
    def twoSum(self, nums: list[str], target: int) -> list[int]:
        for ind, num in enumerate(nums):
            completent = target - num
            if completent in nums[ind+1:]:
                return ind, nums[ind+1:].index(completent) + (ind+1)

# using hash-map : dictionary
class Solution4:
    def twoSum(self, nums: list[str], target: int) -> list[int]:
        nums_map = {}
        # search target - num in dictionary
        for ind, num in enumerate(nums):
            if (target - num in nums_map) and (ind != nums_map[target-num]):
                return ind, nums_map[target-num]
            nums_map[num] = ind
        return None


# using two pointers
class Solution5:
    def twoSum(self, nums: list[str], target: int) -> list[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums) -1
        while not left == right:
            if sorted_nums[left][1] + sorted_nums[right][1] > target:
                right -=1
            elif sorted_nums[left][1] + sorted_nums[right][1] < target:
                left += 1
            else:
                return sorted_nums[left][0], sorted_nums[right][0]
        return None


nums = [3, 2, 3]
target = 6
print(Solution5().twoSum(nums, target))