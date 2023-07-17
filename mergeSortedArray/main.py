# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1+nums2
        nums4 = [item for item in nums3 if item != 0]
        nums5= []
        for item in range(len(nums4)):
            nums5.append(nums4[item])
        nums5.sort()
        print(nums5)
        
        # nums1 = [item for item in nums1 if item != 0]

result = Solution()

result.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)