"""
Given an integer array nums, find a contiguous non-empty subarray
    within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_min_value = nums[0]
        prev_max_value = nums[0]
        product_max = nums[0]

        for num in nums[1:]:
            curr_min_value = min(num, num * prev_min_value, num * prev_max_value)
            curr_max_value = max(num, num * prev_min_value, num * prev_max_value)

            product_max = max(product_max, curr_min_value, curr_max_value)

            prev_min_value = curr_min_value
            prev_max_value = curr_max_value

        return product_max


assert Solution().maxProduct([2, 3, -2, 4]) == 6
assert Solution().maxProduct([-2, 0, -1]) == 0
assert Solution().maxProduct([-2, 3, -4]) == 24
