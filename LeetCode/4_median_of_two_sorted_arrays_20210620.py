class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # smaller one : num1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        ind1 = len(nums1) // 2
        ind2 = len(nums2) // 2
        
        while (nums1[ind1] == nums2[ind2]) or 


        