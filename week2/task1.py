"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        bukv = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        all_combinations = []

        def get_all_comb(chislo, comb, num):
            if len(chislo) == len(comb):
                all_combinations.append(comb)
                return
            for i in range(len(bukv[chislo[num]])):
                get_all_comb(chislo, comb + bukv[chislo[num]][i], num + 1)

        get_all_comb(digits, "", 0)
        if len(all_combinations) == 1:
            all_combinations = []
        return all_combinations


answer = Solution()
print(answer.letterCombinations("23"))
print(answer.letterCombinations(""))
