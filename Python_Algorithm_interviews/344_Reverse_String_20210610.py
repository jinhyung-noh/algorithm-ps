class Solution:
    def reverseString(self, s: list) -> None:   
        length = len(s)
        for i in range(length // 2):
            s[i], s[length -1 -i] = s[length -1 -i], s[i]
        
        return None

# solution in book
class Solution2:
    def reverseString(self, s: list) -> None: 
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right += 1

# "pythonic way"
class Solution3:
    def reverseString(self, s: list) -> None:
        s.reverse()


s = ["h","e","l","l","o"]
print(s)
Solution().reverseString(s)
print(s)

# def testfunc(listA):
#     listA[0], listA[-1] = listA[-1], listA[0]
#     return None

# s = [1,2,3,4,5]
# print(s)
# testfunc(s)
# print(s)