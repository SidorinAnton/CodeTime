"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows  # 3 row => ["", "", ""]
        path_step = 1
        curr_line = 0

        for char in s:
            if len(rows) == 1:  # ABC, 1 row => ABC
                return s

            rows[curr_line] += char
            curr_line += path_step  # 3 rows => 0, 1, 2, 1, 0, 1 ...

            if curr_line == 0 or curr_line == numRows - 1:  # Up or Down of zigzag
                path_step *= -1  # Switch direction

        return "".join(rows)


assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert Solution().convert("A", 1) == "A"
assert Solution().convert("AB", 1) == "AB"
