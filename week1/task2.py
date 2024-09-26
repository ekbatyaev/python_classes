"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/string-to-integer-atoi/description/
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        str_number = ""
        number = 0
        final_znak = ""
        flag = 0
        detected = 0
        digit_flag = 0
        for i in range(len(str)):
            if (
                not str[i].isdigit()
                and (str[i] != "-")
                and (str[i] != "+")
                and (str[i] != " ")
            ):
                break
            elif (
                ((str[i] == "-") or (str[i] == "+"))
                and (flag != 1)
                and (digit_flag != 1)
            ):
                final_znak = str[i]
                flag = 1
            elif (
                ((str[i] == "-") or (str[i] == "+"))
                and (flag == 1)
                and (digit_flag != 1)
            ):
                str_number = ""
                break
            elif (
                ((str[i] == "-") or (str[i] == "+"))
                and (flag == 1)
                and (digit_flag == 1)
            ):
                break
            elif (
                ((str[i] == "-") or (str[i] == "+"))
                and (flag != 1)
                and (digit_flag == 1)
            ):
                break
            elif str[i] != " " and str[i].isdigit():
                str_number += str[i]
                digit_flag = 1
            elif str[i] == " " and digit_flag == 1:
                break
            elif str[i] == " " and detected == 0:
                detected = 1
            elif str[i] == " " and detected == 1 and flag == 1:
                break

        if str_number == "":
            str_number = "0"
        number = int(str_number)
        if final_znak == "-":
            number = -number
        if number > 2**31 - 1:
            number = 2**31 - 1
        elif number < -(2**31):
            number = -(2**31)

        return number


answer = Solution()
print(answer.myAtoi("-5-"))
print(answer.myAtoi("0-1"))
print(answer.myAtoi("  -042"))
print(answer.myAtoi(" +0 123"))
print(answer.myAtoi(" +8213123 111"))
print(answer.myAtoi("3232 ewew"))
print(answer.myAtoi("0  123"))
