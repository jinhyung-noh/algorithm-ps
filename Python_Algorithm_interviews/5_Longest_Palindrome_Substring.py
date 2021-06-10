class Solution:
    def longestPalindrome(self, s: str) -> str:
        lower_s = s.lower()
        answer = []

        # find odd-length palindrome
        for i in range(len(lower_s)):
            j = 0
            while i - j >= 0: 
                try:
                    if lower_s[i-j] == lower_s[i+j]:
                        j += 1
                    else:
                        break
                except IndexError:
                    break
            # answer is not lower case ; 
            answer.append(s[i-j+1:i+j])
            # find even-length palindrome
        for i in range(len(lower_s)):
            j = 0
            while i - j >= 0:
                try:
                    if lower_s[i-j] == lower_s[i+j+1]:
                        j += 1
                    else:
                        break
                except IndexError:
                    break
            if j != 0:
                answer.append(s[i-j+1:i+j+1])

        return sorted(answer, key=len, reverse=True)[0]


# solution in Book ; change some numbers in "expand" function
class Solution2:
    def longestPalindrome(self, s:str) -> str:
        # chech whether palindrome and expand two pointers
        def expand(s: str, left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left + 1: right - 1]
        
        # exception case: return very fast
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, 
                            expand(i, i+1),     # even case
                            expand(i, i+2),     # odd case
                            key=len)
        return result

class Solution3:
    def longestPalindrome(self, s:str) -> str:
        # chech whether palindrome and expand two pointers
        def expand(s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        # exception case: return very fast
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, 
                            expand(i, i+1),     # even case
                            expand(i, i+2),     # odd case
                            key=len)
        return result
s = "SQQSYYSQQS"
print(Solution3().longestPalindrome(s))