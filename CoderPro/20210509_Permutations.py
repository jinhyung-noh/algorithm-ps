# my solution using recursion
class Solution1():
    def getPMTList(self, ls):
        # return a permutation set : list of list
        result = []                      # list of list
        if len(ls) == 1:
            return [ls]
        for i in range(len(ls)):      # 인수로 받은 list 중 하나씩 제외하고 (n-1)의 인수를 가진 list에 대해 recursion
            for j in self.getPMTList(ls[:i] + ls[i+1:]): # (n-1)버전의 getPMTList가 lol(list of list)를 반환하므로 각각에 대해
                result += [[ls[i]] + j]                  # 빠졌던 원소를 처음에 넣어 permutation 완성 후 빈 list []에 추가 후 반환
        return result


# solution of TechLead  -- 너무 어려운데??
class Solution2():
    def permute1(self, nums, start=0):          # start는 swap할 자릿수
        if start == len(nums) - 1:              # base case : 마지막 자릿수 도달하면 lol 반환
            return [nums[:]]

        result = []
        for i in range(start, len(nums)):             # start 자릿수에서 swap 진행
            nums[start], nums[i] = nums[i], nums[start]
            result += self.permute1(nums, start + 1)      # 이후 다음 자릿수에서 swap 진행한것 추가(recursion)
            nums[start], nums[i] = nums[i], nums[start]         # swwp 진행 후 되돌려놓기 (다음 swap을 위해)
        return result


    def permute2(self, nums, values=[]):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            result += self.permute2(nums[:i] + nums[i + 1:], values + [nums[i]])  # 앞자리부터 하나씩 빼서 value list에 첨가
        return result                                                             # 빼는 순서를 permutation으로!

    def permute2Iterative(self, nums):
        results = []
        stack = [(nums, [])]
        while len(stack):
          nums, values = stack.pop()
          if not nums:
            results += [values]
          for i in range(len(nums)):
            stack.append((nums[:i]+nums[i+1:], values+[nums[i]]))
        return results


# # print(Solution2().permute([1, 2, 3]))
# print(Solution2().permute2([1, 2, 3]))
#
#
listA = [1, 2, 3]
answer = Solution1().getPMTList(listA)
print(answer)
print(len(answer))
