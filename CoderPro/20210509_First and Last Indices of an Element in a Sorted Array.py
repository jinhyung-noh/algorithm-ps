# my solution (binary search by recursion)
class Solution1():
    def getLowIndexHelper(self, ls, target, low, high):
        # binary search by recursion
        if low == high:
            return low
        mid_ind = (low + high) // 2
        if ls[mid_ind] >= target:
            return Solution1().getLowIndexHelper(ls, target, low, mid_ind)
        else:
            return Solution1().getLowIndexHelper(ls, target, mid_ind + 1, high)

    def getHighIndexHelper(self, ls, target, low, high):
        # binary search by recursion
        if low == high:
            return high
        mid_ind = (low + high + 1) // 2  # 1을 더해준 이유 : 오른쪽을 탐색해야 하므로 중심을 가운데, 혹은 오른쪽에 치우치게 만듦
        if ls[mid_ind] <= target:
            return Solution1().getHighIndexHelper(ls, target, mid_ind, high)
        else:
            return Solution1().getHighIndexHelper(ls, target, low, mid_ind - 1)

    def getTwoIndices(self, ls, target):
        low_ind = Solution1().getLowIndexHelper(ls, target, 0, len(ls) - 1)
        high_ind = Solution1().getHighIndexHelper(ls, target, 0, len(ls) - 1)
        return (low_ind, high_ind)


# my solution (binary search by iteration)
class Solution2():
    def getTwoIndices(self, ls, target):
        low_ind = Solution2().getLowIndexHelper(ls, target)
        high_ind = Solution2().getHighIndexHelper(ls, target)
        return (low_ind, high_ind)

    def getLowIndexHelper(self, ls, target):
        low = 0
        high = len(ls) - 1
        while True:
            if low == high:
                break
            mid = (low + high) // 2     # 왼쪽을 탐색하고 싶기 때문에 mid를 가운데, 혹은 왼쪽으로 지정하고
            if ls[mid] >= target:       # mid와 같을 경우를 왼쪽에 포함
                high = mid
            else:
                low = mid + 1
        return low

    def getHighIndexHelper(self, ls, target):
        low = 0
        high = len(ls) -1
        while True:
            if low == high:
                break
            mid = (low + high + 1) // 2  # 오른쪽을 탐색하고 싶기 때문에 mid를 가운데, 혹은 오른쪽으로 지정하고
            if ls[mid] <= target:        # mid와 같을 경우를 오른쪽에 포함
                low = mid
            else:
                high = mid - 1
        return high


# solution by TechLead (binary search by recursion)
class Solution3():
    def getRange(self, arr, target):
        first = self.binarySearch(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearch(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearch(self, arr, low, high, target, findFirst):
        if high < low:
            return -1
        # mid = low + (high - low) // 2   # 왼쪽에 치우친 중심 인덱스
        mid = (low + high) // 2           # 마찬가지
        if findFirst:  # findFirst == True ; 왼쪽 인덱스
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid
            if target > arr[mid]:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)
            else:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
        else:
            if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                return mid
            if target < arr[mid]:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
            else:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)


# solution by TechLead (binary search by iteration)
class Solution4():
    def getRange(self, arr, target):
        first = self.binarySearch(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearch(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearch(self, arr, low, high, target, findFirst):
        while True:
            if high < low:
                return -1
            # mid = low + (high - low) // 2   # 왼쪽에 치우친 중심 인덱스
            mid = (low + high) // 2           # 마찬가지
            if findFirst:  # findFirst == True ; 왼쪽 인덱스
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                if target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


sorted_list = [1, 3, 3, 5, 7, 7, 8, 9, 9, 15]
target_num = 7


# answer = Solution1().getLowIndexHelper(sorted_list, target_num, 0, len(sorted_list) - 1)
# answer = Solution1().getHighIndexHelper(sorted_list, target_num, 0, len(sorted_list) - 1)
# answer = Solution1().getTwoIndices(sorted_list, target_num)

# answer = Solution2().getLowIndexHelper(sorted_list, target_num)
# answer = Solution2().getTwoIndices(sorted_list, target_num)

# answer = Solution3().getRange(sorted_list, target_num)
answer = Solution4().getRange(sorted_list, target_num)

print(answer)

