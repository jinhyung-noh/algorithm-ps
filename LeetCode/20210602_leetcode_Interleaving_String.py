class Solution:
    """return True/ False"""
    def isInterleave(self, s1, s2, s3):
        return self._isInterleaveHelper(s1, s2, self._str2dict(s3), [], 0)

    # return list of s2 candidates
    def _isInterleaveHelper(self, s1, s2, hashmap, indices, ind):
        """
        s1      : 
        s2      :
        hashmap : a hashmap made from string to check whether s1, s2 ...
        indices : recording s1 indices  
        ind     : next index of s1
        """
        # 끝까지 간 경우
        if ind >= len(s1):
            return s2 == self._dict2str(hashmap, indices)
        if s1[ind] not in hashmap:
            return False 
        else:
            # base case : 다음 문자가 마지막 문자의 ind보다 작을때
            if len(indices) > 0 and (max(hashmap[s1[ind]]) <= indices[-1]):
                return []
            for i in hashmap[s1[ind]]:
                if len(indices) == 0 or i > indices[-1]:
                    indices.append(i)
                    result = self._isInterleaveHelper(s1, s2, hashmap, indices, ind+1)
                    indices.pop()
                    if result:
                        return result
        return False

    # string to dict
    def _str2dict(self, string):
        result = {}
        for ind in range(len(string)):
            if string[ind] in result:
                result[string[ind]].append(ind)
            else:
                result[string[ind]] = [ind]
        return result

    # dictionary to string
    def _dict2str(self, hashmap, indices):
        # length of string
        str_len = 0
        for char in hashmap:
            str_len += len(hashmap[char])
        # make list ; each element is char 
        result = [''] * str_len
        for char, nums in hashmap.items():
            for num in nums:
                result[num] = char

        for i in indices:
            result[i] = ''

        result = ''.join(result)
        return result
        

            

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# hashmap = Solution()._str2dict(s3)
# print(hashmap)
# print(Solution()._dict2str(hashmap, [0, 1, 6, 7, 9]))
# print(Solution()._isInterleaveHelper(s1, hashmap, [], 0))
s1 = ""; s2 = ""; s3 = ""
# s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
# s1 = 'def'; s2 = ''; s3 = 'de'
# s1 = "cabbacccabacbcaabaccacacc"
# s2 = "bccacbacabbabaaacbbbbcbbcacc"
# s3 = "cbccacabbacabbbaacbcacaaacbbacbcaabbbbacbcbcacccacacc"
print(Solution().isInterleave(s1, s2, s3))
