"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counter = {}  # char: (idx, freq_in_string)

        for idx, char in enumerate(s):
            if char_counter.get(char):
                counter = char_counter[char][1]  # freq_in_string
                char_counter[char] = (idx, counter + 1)  # Here index is irrelevant
            else:
                char_counter[char] = (idx, 1)

        for idx, freq in char_counter.values():
            if freq == 1:
                return idx

        return -1


assert Solution().firstUniqChar("leetcode") == 0
assert Solution().firstUniqChar("loveleetcode") == 2
assert Solution().firstUniqChar("aabb") == -1
