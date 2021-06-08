# my Solution
class Solution():
    def reconstByHeight(self, ls):
        result = []
        sorted_list = self.sortList(ls)  # 이미 정렬된 list 사용
        n = len(ls)
        for i in range(n):               # 정렬된 상태이므로 각각의 사람의 두번째 수(보이는 사람수)를 index를 가지도록 추가해준다
            result.insert(sorted_list[i][1], sorted_list[i])
        return result

    def sortList(self, ls):
        result = ls[:]
        n = len(ls)
        for i in range(n):
            for j in range(i):
                if result[i][0] > result[j][0]:  # 첫번째 키로 정렬
                    result[i], result[j] = result[j], result[i]
                elif result[i][0] == result[j][0] and result[i][1] < result[j][1]:  # 키가 같을 경우 보이는 순서로 정렬
                    result[i], result[j] = result[j], result[i]
        return result


# Solution by TechLead
class Solution1:
    def reconstructQueue(self, imput):
        input.sort(key=lambda x:          # sort 진행 : 키 내림차순, 번호 오름차순
                   (-x[0], x[1])          # == (-키, 번호) 오름차순
                   )
        result =[]
        for person in input:
            result.insert(person[1], person)
        return result

input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
# answer = Solution().reconstByHeight(input)
# print(answer)
# sorted_list = Solution().sortList(input)
# print(sorted_list)

print(Solution1().reconstructQueue(input))


