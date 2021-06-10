# my solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = self._only_alphabet(s).lower()
        if alpha_s == alpha_s[::-1]:
            return True
        else:
            return False

    def _only_alphabet(self, s):
        s_list = list(s)
        for ind, char in enumerate(s_list):
            if not char.isnumeric() and not char.isalpha():
                s_list[ind] = ''
        return ''.join(s_list)

# solutions in Book
class Solution2():
    def isPalindrome(self, s:str) -> bool:
        # preprocessing : only lower case alpahbet and numbers
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # determine whether s is a palindrome
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():   # pop() returns removed value!
                return False        

        return True

# solution using collections.deque
class Solution2:
    def isPalindrome(self, s):
        # deque datatype for time saving
        from collections import deque
        strs : deque = deque()

        # preprocessing
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


class Solution3:
    def isPalindrome(self, s):
        import re

        s = s.lower()
        # string filtering by re(reqular expression)
        s = re.sub('\W', '', s)

        return s == s[::-1]
s = "A man, a plan, a canal: Panama"



print(Solution2().isPalindrome(s))
