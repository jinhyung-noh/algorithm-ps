class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(len(nums)) if i % 2 == 0])


class Solution2:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)//2):
            result += nums[2*i]
        return result

# solution in Book : pythonic way
class Solution3:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])