class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        hash = defaultdict(lambda: None)

        for idx, char in enumerate(s):
            if hash[char] is not None:
                return max(idx, self.lengthOfLongestSubstring(s[hash[char]+1:]))
            hash[char] = idx 

        return len(s)
        

# solution in Book
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # if a character appear again --> renew 'start'
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:   # renew max_length
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length


s = "fakjwowefasd"

print(Solution2().lengthOfLongestSubstring(s))