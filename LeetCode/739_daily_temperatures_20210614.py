class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        remaining_days = []

        for today, today_temp in enumerate(temperatures):
            while remaining_days and temperatures[remaining_days[-1]] < today_temp:
                cold_day = remaining_days.pop()
                result[cold_day] = today - cold_day
            remaining_days.append(today)
            
        return result


# solution in Book
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """exactly same above..."""
        pass
        return None
temperatures = [30,60,90]
print(Solution().dailyTemperatures(temperatures))