class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def combine_helper(num, stack):

            # base case
            if len(stack) == k:
                result.append(stack[:])
                return None

            if num == n+1:
                return

            for next_num in range(num, n+1):
                stack.append(next_num)
                combine_helper(next_num+1, stack)
                stack.pop()

        result = []    
        stack =[]
        combine_helper(1, stack)
        return result


# solution in Book
class Solution2:
    def combine(self, n: int, k: int) -> list[list[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
            
        dfs([], 1, k)
        return results


class Solution3:
    def combine(self, n: int, k: int) -> list[list[int]]:
        import itertools
        return list(itertools.combinations(range(1, n+1), k))


print(Solution3().combine(4,2))