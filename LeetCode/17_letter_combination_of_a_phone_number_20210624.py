class Solution:
    def _letterCombinations_helper(self, digits: str, index=0) -> list[str]:
        keypad = {
            1: [''],
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z'],
            0: ['']
        }
        ind = index
        if ind >= len(digits):
            return ['']
        result = []
        for char in keypad[int(digits[ind])]:
            result += [char+chars for chars in self._letterCombinations_helper(digits, ind+1)]
        return result

    def letterCombinations(self, digits: str) -> list[str]:
        result =  self._letterCombinations_helper(digits)
        return result if result != [''] else []


class Solution2:
    def letterCombinations(self, digits: str) -> list[str]:
        def _dfs_helper(index=0, word=''):
            # base case
            if index >= len(digits):
                return

            for char in keypad[int(digits[index])]:
                if index >= len(digits) - 1:
                    words.append(word + char)
                _dfs_helper(index+1, word+char)

        keypad = {
            1: [''],
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z'],
            0: ['']
        }
        words = []
        _dfs_helper()
        return words

    
# solution in Book
class Solution3:
    def letterCombinations(delf, digits: str) -> list[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return None

            for i in range(index, len(digits)):
                # iterate all characters correspond to i
                for char in dic[digits[i]]:
                    dfs(i+1, path + char)

        # exception case
        if not digits:
            return []
        
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        dfs(0,"")
        return result


# revision of solution3
# 339p
class Solution4:
    def letterCombinations(delf, digits: str) -> list[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return None

            for char in dic[digits[index]]:
                dfs(index+1, path + char)

        # exception case
        if not digits:
            return []
        
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        dfs(0,"")
        return result

digits = "222"
print(Solution4().letterCombinations(digits))