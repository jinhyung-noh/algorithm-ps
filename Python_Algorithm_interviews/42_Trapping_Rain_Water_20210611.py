class Solution:
    def trap(self, heights: list[int]) -> int:
        from collections import Counter
        hash = Counter(heights)

        # exception case
        if not heights:
            return 0

        trapped_water = 0
        between = 0
        for level in range(max(hash), 0, -1):
            # left index
            for ind in range(len(heights)):
                if heights[ind] >= level:
                    left = ind
                    break
            # right index
            for ind in range(len(heights)-1,-1,-1):
                if heights[ind] >= level:
                    right = ind
                    break
            # between left, right : all pillars where its height is 
            #                       greater or equal than "level"
            try:
                between += hash[level]
            except:
                pass
            trapped_water += right - left + 1 - between

        return trapped_water



# solution in book
# solution using 2 pointers
class Solution2:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max),    \
                                    max(height[right], right_max)
        
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


# solution using stack
class Solution3:
    def trap(self, heght: list[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # turning point : higher than just before
            while stack and height[i] > height[stack[-1]]:
                # pop from stack
                top = stack.pop()

                if not len(stack):
                    break

                # water height 
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume


height = [5,5,1,7,1,1,5,2,7,6]
print(Solution3().trap(height))