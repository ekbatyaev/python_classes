"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_integer = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        roman_conv = ""

        def rim_version(num: int) -> str:
            str_version = ""
            if num >= 1000:
                str_version = roman_integer[1000] * (num // 1000)
                return str_version
            elif num == 900:
                str_version = roman_integer[100] + roman_integer[1000]
                return str_version
            elif num >= 500:
                str_version = roman_integer[500]
                return str_version
            elif num == 400:
                str_version = roman_integer[100] + roman_integer[500]
                return str_version
            elif num >= 100:
                str_version = roman_integer[100] * (num // 100)
                return str_version
            elif num == 90:
                str_version = roman_integer[10] + roman_integer[100]
                return str_version
            elif num >= 50:
                str_version = roman_integer[50]
                return str_version
            elif num == 40:
                str_version = roman_integer[10] + roman_integer[50]
                return str_version
            elif num < 40:
                while num > 0:
                    if num - 10 >= 0:
                        num -= 10
                        str_version += roman_integer[10]
                    else:
                        break
                if num == 9:
                    str_version += roman_integer[1] + roman_integer[10]
                    return str_version

                while num > 0:
                    if num - 5 >= 0:
                        num -= 5
                        str_version += roman_integer[5]
                    else:
                        break
                if num == 4:
                    str_version += roman_integer[1] + roman_integer[5]
                    return str_version

                while num > 0:
                    if num - 1 >= 0:
                        num -= 1
                        str_version += roman_integer[1]
                    else:
                        break

                return str_version

        roman_conv += rim_version(((num // 1000) * 1000))
        num -= (num // 1000) * 1000
        if num < 900:
            roman_conv += rim_version(((num // 500) * 500))
            num -= (num // 500) * 500

        else:
            roman_conv += rim_version(((num // 100) * 100))
            num -= (num // 100) * 100

        roman_conv += rim_version((num // 100) * 100)
        num -= (num // 100) * 100

        if num < 90:
            roman_conv += rim_version(((num // 50) * 50))
            num -= (num // 50) * 50
        else:
            roman_conv += rim_version(((num // 10) * 10))
            num -= (num // 10) * 10

        roman_conv += rim_version((num // 50) * 50)
        num -= (num // 50) * 50

        if num > 40 and num <= 49:
            roman_conv += rim_version((num // 10) * 10)
            num -= (num // 10) * 10

            roman_conv += rim_version(num)
            num = 0
        else:
            roman_conv += rim_version(num)
            num -= num

        return roman_conv


answer = Solution()
print(answer.intToRoman(3749))
print(answer.intToRoman(58))
print(answer.intToRoman(1994))
print(answer.intToRoman(400))
