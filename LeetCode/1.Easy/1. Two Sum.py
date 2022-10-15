"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Create some hash table (like dict, were key is number and value is index).
        Go through numbers. Then we make diff between target and number (targe - num).
            If diff not in dict --> put current number there.
            If result in dict => we processed it => targe = current number + number in dict.
        If there is no such number (all values were processed) --> return []
        """
        processed_numbers = {}

        for num_idx in range(len(nums)):
            current_numer = nums[num_idx]
            diff = target - current_numer

            if processed_numbers.get(diff) is None:
                processed_numbers[current_numer] = num_idx
            else:
                return sorted([num_idx, processed_numbers[diff]])

        return []


assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
assert Solution().twoSum([3, 3], 6) == [0, 1]
assert Solution().twoSum([3, 3], 7) == []
assert Solution().twoSum([], 7) == []
