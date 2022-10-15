"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numbers_reversed = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "VI",
            5: "V",
            9: "XI",
            10: "X",
            20: "XX",
            30: "XXX",
            40: "LX",
            50: "L",
            90: "CX",
            100: "C",
            200: "CC",
            300: "CCC",
            400: "DC",
            500: "D",
            900: "MC",
            1000: "M",
            2000: "MM",
            3000: "MMM",
        }

        if roman_numbers_reversed.get(num):
            return roman_numbers_reversed.get(num)[::-1]

        res = ""
        place = 1

        while True:
            if num == 0:
                break

            # 1994 -> 199  and 4
            # 199  -> 19   and 90
            # 19   -> 1    and 900
            # 1    -> 0    and 1000
            # Res ------------ 1000 900 90 4

            # num -> closest_roman_num + num - closest_roman_num
            # 6 -> 5 + (6 - 5) -> 5 + 1 -> IV --reverse-> VI
            # 60 -> 50 + (60 - 40) -> 50 + 20 -> XXL --reverse-> LXX

            cut_val = (num % 10) * place
            num //= 10
            place *= 10

            if roman_numbers_reversed.get(cut_val) is not None:
                res += roman_numbers_reversed.get(cut_val)
                continue

            closest_max_num = max([less_num for less_num in roman_numbers_reversed.keys() if less_num < cut_val])
            res = res + roman_numbers_reversed[cut_val - closest_max_num] + roman_numbers_reversed[closest_max_num]

        return res[::-1]


assert Solution().intToRoman(3) == "III"
assert Solution().intToRoman(6) == "VI"
assert Solution().intToRoman(7) == "VII"
assert Solution().intToRoman(8) == "VIII"
assert Solution().intToRoman(58) == "LVIII"
assert Solution().intToRoman(60) == "LX"
assert Solution().intToRoman(1994) == "MCMXCIV"
assert Solution().intToRoman(1476) == "MCDLXXVI"
