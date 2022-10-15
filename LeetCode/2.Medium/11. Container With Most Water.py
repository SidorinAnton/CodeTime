"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
    In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        OX - step between values in array
        OY - values in array
        res = maximum of OX * OY

           [2, 1, 3] -- input
        3 |       O
        2 | O     O
        1 | O  O  O
          +-------
            1  2  3

        Values = [
          2 - 1 => min(2, 1) * 1
          2 - 3 => min(2, 3) * 2
          1 - 3 => min(1, 3) * 1
        ]

        Res = min(height_1, height_2) * (idx_2 - idx_1)
        """
        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while True:
            if left_pointer >= right_pointer:
                break

            min_height = min(height[left_pointer], height[right_pointer])
            width = right_pointer - left_pointer
            area = min_height * width

            if max_area < area:
                max_area = area

            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area

    def maxAreaSlow(self, height: List[int]) -> int:
        max_area = 0
        tmp_height = height[:]

        while len(tmp_height) != 1:
            last_val = tmp_height.pop()

            for val_idx in range(len(tmp_height)):
                min_height = min(last_val, tmp_height[val_idx])
                width = len(tmp_height) - val_idx
                area = min_height * width
                if max_area < area:
                    max_area = area

        return max_area


assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution().maxArea([1, 1]) == 1
assert Solution().maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
