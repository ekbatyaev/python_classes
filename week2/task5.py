"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/count-and-say/description/
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        def rec_solution(num) -> str:
            if num == 1:
                return "1"
            ans = rec_solution(num - 1)
            chislo = ans
            pr = ""
            count = 1

            for i in range(1, len(chislo)):
                if chislo[i] == chislo[i - 1]:
                    count += 1
                else:
                    pr += str(count) + chislo[i - 1]
                    count = 1

            pr += str(count) + chislo[-1]
            return pr

        return rec_solution(n)


answer = Solution()
print(answer.countAndSay(4))
