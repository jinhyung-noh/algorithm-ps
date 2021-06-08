class Solution():
    # my solution using hashmap
    def sort1(self, ls):
        from collections import defaultdict

        hashmap = defaultdict(lambda: 0)
        for i in ls:
            hashmap[i] +=1
        result =  [1] * hashmap[1]   \
                + [2] * hashmap[2]   \
                + [3] * hashmap[3]
        return result

    # sol by TechLead
    def sortNums(self, nums):        # one_index는 왼쪽에서 시작, three_index는 오른쪽에서 시작하고
        one_index = 0                # index가 오른쪽으로 이동하면서 1은 왼쪽, 3은 오른쪽으로 swapping을 통해
        three_index = len(nums) - 1  # 보내버리면 왼쪽에는 1만, 오른쪽에는 3만 남게 된다
        index = 0
        while index <= three_index:
            if nums[index] == 1:
                nums[index], nums[one_index] = nums[one_index], nums[index]
                one_index +=1
                index += 1
            elif nums[index] == 2:
                index += 1
            elif nums[index] == 3:
                nums[index], nums[three_index] = nums[three_index], nums[index]
                three_index -= 1
        return nums

listA = [3, 3, 1, 2, 3, 2, 2, 3, 1, 1, 2]
listB = [2,2,2,2,3,2,1,2,2,2]
answer = Solution().sort1(listA)
answer2 = Solution().sortNums(listB)
print(answer2)