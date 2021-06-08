
class Solution(object):
    # my solution
    def getTwoIndex(self, ls, target):
        result = set()
        for i in ls:
            if (target - i) in ls:
                result.add(ls.index(i))
                result.add(ls.index(target - i))
        result = list(result)
        return result

    # Sol1 by TechLead ; O(n**2) time complexity / no space complexity
    def TwoSum1(self, ls, target):
        for ind_a, a in enumerate(ls):      ## enumerate(iterable_seq) --> (ind, seq[ind])
            for ind_b, b in enumerate(ls):
                if a == b:
                    continue
                if a + b == target:
                    return [ind_a, ind_b]

    # Sol2 by TechLead ; O(n) time, space complexity
    def TwoSum2(self, ls, target):
        values = {}
        for ind, num in enumerate(ls):            # list 한번만 순회함
            values[num] = ind
            if (target - num) in values:
                return [values[target - num], ind]

ls = [2, 7, 11, 15]
target = 18

answer1 = Solution().getTwoIndex(ls, target)
answer2 = Solution().TwoSum1(ls, target)
answer3 = Solution().TwoSum2(ls, target)
print(answer3)
