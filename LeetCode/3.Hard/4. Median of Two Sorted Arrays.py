"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List


class Solution:
    # O(n + m)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = []

        first_arr_pointer = 0
        second_arr_pointer = 0

        while True:
            if first_arr_pointer == len(nums1):
                break
            if second_arr_pointer == len(nums2):
                break

            if nums1[first_arr_pointer] > nums2[second_arr_pointer]:
                sorted_array.append(nums2[second_arr_pointer])
                second_arr_pointer += 1
            else:
                sorted_array.append(nums1[first_arr_pointer])
                first_arr_pointer += 1

        sorted_array = sorted_array + nums1[first_arr_pointer:] + nums2[second_arr_pointer:]

        if len(sorted_array) == 0:
            return

        if len(sorted_array) % 2 == 0:  # even
            mid_minus = len(sorted_array) // 2 - 1
            mid_plus = mid_minus + 1
            return (sorted_array[mid_minus] + sorted_array[mid_plus]) / 2
        else:  # odd
            return sorted_array[len(sorted_array) // 2]


# Solution().findMedianSortedArrays([1, 3], [2, 7])  # 1, 2, 3, 7 -> 2.5
# Solution().findMedianSortedArrays([1, 3], [2, 7, 8])  # 1, 2, 3, 7, 8 -> 3
# Solution().findMedianSortedArrays([1, 3, 4], [2, 7, 8])  # 1, 2, 3, 4, 7, 8 -> 3.5
# Solution().findMedianSortedArrays([5, 6, 7], [1, 2, 3])  # 1, 2, 3, 5, 6, 7 -> 4
# Solution().findMedianSortedArrays([], [1, 2, 3])  # 1, 2, 3 -> 2
# Solution().findMedianSortedArrays([5, 6, 7], [])  # 5, 6, 7 -> 6
# Solution().findMedianSortedArrays([], [])  # None -> None
assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert Solution().findMedianSortedArrays([], []) is None
assert Solution().findMedianSortedArrays([], [2]) == 2
assert Solution().findMedianSortedArrays([2], []) == 2
assert Solution().findMedianSortedArrays([1, 2, 3, 4, 5], []) == 3
assert Solution().findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9]) == 5
assert Solution().findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8]) == 4.5
assert Solution().findMedianSortedArrays([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]) == 0.0
