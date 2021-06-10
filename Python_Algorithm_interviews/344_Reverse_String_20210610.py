class Solution:
    import typing
    def reverseString(self, s: List[str]) -> None:   
        length = len(s)
        for i in range(length // 2):
            s[i], s[length -1 -i] = s[length -1 -i], s[i]
        
        return None

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