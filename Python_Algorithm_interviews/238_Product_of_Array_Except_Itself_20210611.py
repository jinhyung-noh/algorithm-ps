# using division...
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        
        # 2 more zeros
        if zero_count >= 2:
            return [0] * len(nums)

        products = 1
        for num in nums:
            if num != 0:
                products *= num
        # 1 zero
        if zero_count == 1:
            return [0 if num != 0 else products for num in nums]
        # no zero
        else:
            return [products // num for num in nums]

# using hashmap
class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        from collections import Counter
        hash = Counter(nums)
        result = []
        for num in nums:
            each_result = 1
            for key in hash:
                if key == num:
                    each_result *= key ** (hash[key]-1)
                else:
                    each_result *= key ** hash[key]
            result.append(each_result)
        return result


# solution in Book
class Solution3:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out = []
        p = 1
        # left production
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]

        p = 1
        # right production
        for i in range(len(nums)-1, -1, -1):
            out[i] *= p
            p *= nums[i]
        
        return out
nums = [1,2,3,4]
print(Solution3().productExceptSelf(nums))