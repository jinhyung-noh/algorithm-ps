import heapq

arr = []

numbers = [3,1,4,2,5]

# for number in numbers:
# 	heapq.heappush(arr, number)

heapq.heapify(numbers)
print(numbers)

# print(heapq.heappop(arr), arr)
