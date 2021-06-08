# my solution
class Solution(object):
    # using hashmap
    def findNonDup1(self, ls):
        from collections import defaultdict
        # create hashmap
        hashmap = defaultdict(lambda: 0)
        for num in ls:
            hashmap[num] += 1
        for num in hashmap:
            if hashmap[num] == 1:
                return num

    # sol by TechLead
    # using hashmap
    def singleNumber1(self, nums):
        occurence ={}
        for n in nums:
            occurence[n] = occurence.get(n, 0) + 1
        for key, val in occurence.items():
            if val == 1:
                return key

    # sol using XOR operator ^
    # a^b == a+b (a != b)
    #        0   (a == b)
    def singleNumber2(self,nums):
        unique = 0
        for n in nums:
            unique ^= n
        return unique





listA = [4, 3, 2, 4, 1, 3, 2]
# answer = Solution().findNonDup1(listA)
# answer = Solution().singleNumber1(listA)
answer = Solution().singleNumber2(listA)
print(answer)


