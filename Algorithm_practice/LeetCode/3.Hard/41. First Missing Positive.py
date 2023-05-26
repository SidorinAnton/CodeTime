"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""
from typing import List


class Solution:
    # Space = O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique_nums = set(nums)  # hash table
        num_len = len(unique_nums)

        for min_number in range(1, num_len + 1):
            if min_number not in unique_nums:
                return min_number

        return num_len + 1


assert Solution().firstMissingPositive([1, 2, 0]) == 3
assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2
assert Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1
