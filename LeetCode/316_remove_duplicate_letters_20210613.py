class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []

        for ind in range(len(s)):
            if result == [] or (s[ind] not in result and result[-1] < s[ind]):
                result.append(s[ind])
            else:
                result_tmp = []
                # back to result(stack)
                while result:
                    pop = result.pop()
                    if pop > s[ind] and pop in s[ind:]:
                        pass
                    else:
                        result_tmp.append(pop)
                        break
                result = result + result_tmp[::-1]
                if s[ind] not in result:
                    result.append(s[ind])
                # try:
                #     if s[ind] not in result and s[ind] not in s[ind+1:]:
                #         result.append(s[ind])
                # except IndexError:
                #     if s[ind] not in result:
                #         result.append(s[ind])

        return ''.join(result)

                    
# solution in Book          247p
# using recursion
class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        # set -> sort
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # if whole set == suffix set --> separate
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


# using stack
class Solution3:
    def removeDuplicateLetters(self, s:str) -> str:
        from collections import Counter

        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # remove from stack if there is same character after
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)
s = "bcabc" 
print(Solution().removeDuplicateLetters(s))


