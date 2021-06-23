class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        freqs = Counter(nums)
        freqs_list = [(num, freqs[num]) for num in freqs]
        freqs_list.sort(key=lambda x:-x[1])

        return [freqs_list[i][0] for i in range(k)]


# solution in Book
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        import heapq

        freqs = Counter(nums)
        freqs_heap = []
        # insert heap in descending order
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = []
        # extract k (min_heap)
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


# more pythonic way
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        # Counter.most_common(k) : k most common elements [(elem1, freq1), (elem2, freq2)...]
        # * --> unpack
        # zip --> packing (iterator --> list)
        return list(zip(*Counter(nums).most_common(k)))[0]

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))
