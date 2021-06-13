class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                try:
                    if stack.pop() + char not in ['()', '{}', '[]']:
                        return False
                except:
                    return False
        # empty stack : correct
        if stack == []:
            return True
        # remaining stack : incorrect
        else:
            return False


# solution in Book
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            '[': '[',
        }

        for char in s:
            if char not in table:
                stack.append(char)
            # not stack : if s comes with )}] first, stack is []
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0


s = '))'
print(Solution2().isValid(s))