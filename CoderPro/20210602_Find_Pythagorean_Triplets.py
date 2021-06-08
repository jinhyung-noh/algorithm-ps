class Solution:
    """return a list of pythagorean numbers"""
    def find_pythagorean(self, nums):
        num_sqr = [i*i for i in nums]
        for i in range(len(num_sqr)):
            for j in range(i+1, len(num_sqr)):
                a = num_sqr[i] + num_sqr[j]
                if a in num_sqr:
                    return [nums[i], nums[j], nums[num_sqr.index(a)]]
        return None

            
# Solution by TechLead
# O(n^3), O(1)
def findPythagoreanTriplets(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if a*a + b*b == c*c:
                    return True
    return False

def findPythagoreanTriplets2(nums):
    squares = set([n*n for n in nums])

    for a in nums:
        for b in nums:
            if a*a + b*b in squares:
                return True
    return False


num_list = [3, 5, 12, 5, 13]
print(Solution().find_pythagorean(num_list))
print(findPythagoreanTriplets(num_list))
print(findPythagoreanTriplets2(num_list))