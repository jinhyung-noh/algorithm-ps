def solution(nums):
    hash = {}
    for i in nums:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1

    return min(len(hash), len(nums) // 2)
