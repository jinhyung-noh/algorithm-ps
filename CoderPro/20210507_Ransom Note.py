from collections import defaultdict
# defaultdict


class Solution(object):
    def canSpell(self, magazine, note):
        letters = defaultdict(lambda: 0)
        for c in magazine:
            letters[c] += 1
        for c in note:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        return True


print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
