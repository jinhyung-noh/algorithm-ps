class Solution:
	"""return maximum area ; an integer"""
	def maxArea(self, h, w, horizontalCuts, verticalCuts):
		return self._maxAreaHelper(horizontalCuts) * self._maxAreaHelper(verticalCuts) 
		
	def _maxAreaHelper(self, Cuts):
		a_n = 0
		maximum = 0
		for i in Cuts:
			if i - a_n > maximum:
				maximum  = i - a_n
			a_n = i
		return maximum



h = 5; w = 4; horizontalCuts = [1,2,4]; verticalCuts = [1,3]
# print(Solution()._maxAreaHelper(horizontalCuts))
# print(Solution()._maxAreaHelper(verticalCuts))
print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
