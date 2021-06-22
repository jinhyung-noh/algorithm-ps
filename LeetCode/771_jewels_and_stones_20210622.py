class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int :
        from collections import defaultdict
        result = 0

        stone_dict = defaultdict(int)    
        for char in stones:
            stone_dict[char] += 1
        
        for stone in stone_dict:
            if stone in jewels:
                result += stone_dict[stone]
        return result


# solution in Book
class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int :
        from collections import Counter:
        freqs = Counter(stones)
        count = 0

        for jewel in jewels:
            count += freqs[jewel]
        return count


# "pythonic" way
class Solution3:
    def numJewelsInStones(self, jewels: str, stones: str) -> int :
        return sum(stone in jewels for stone in stones)


jewels = "z"
stones = "ZZ"

print(Solution().numJewelsInStones(jewels, stones))
