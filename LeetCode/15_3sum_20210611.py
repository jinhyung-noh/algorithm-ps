class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        sorted_nums = sorted(nums)
        answer = set()
        for ind in range(len(sorted_nums)):
            left, right = ind + 1, len(sorted_nums) - 1
        
            while left < right:
                if sorted_nums[left] + sorted_nums[right] > -sorted_nums[ind]:
                    right -= 1
                elif sorted_nums[left] + sorted_nums[right] < -sorted_nums[ind]:
                    left += 1
                else:
                    answer.add((sorted_nums[ind],
                                    sorted_nums[left],
                                    sorted_nums[right]))
                    left += 1
                    right -= 1
        return [list(elem) for elem in answer]


# solution in Book
# brute force
class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        # repeat brute-force 3 times
        for i in range(len(nums)-2):
            # jump overlap
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) -1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i],
                                        nums[j],
                                        nums[k]])
        return results


# using two pointers
class Solution3:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # jump overlapped value
            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
    
nums = [-1,0,1,2,-1,-4]
print(Solution3().threeSum(nums))
