"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        # davdaf -> {dav, avd, vdaf}  # Greate res
        # davdaf -> {dav, avd, vdaf, daf, af, f}  # Current res
        """
        possible_substrs = set()

        for idx_char in range(len(s)):
            tmp_str = s[idx_char]
            for idx_next_char in range(idx_char + 1, len(s)):

                if s[idx_next_char] in tmp_str:
                    possible_substrs.add(tmp_str)
                    break

                tmp_str += s[idx_next_char]

            possible_substrs.add(tmp_str)

        max_val = 0
        for substr in possible_substrs:
            if len(substr) > max_val:
                max_val = len(substr)

        return max_val


assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("") == 0
assert Solution().lengthOfLongestSubstring("abcde") == 5
assert Solution().lengthOfLongestSubstring("davdaf") == 4  # vdaf
assert Solution().lengthOfLongestSubstring(" ") == 1  # " "
assert Solution().lengthOfLongestSubstring("a") == 1  # a
