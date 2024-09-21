"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/generate-parentheses/description/
"""


class Solution:
    def generateParenthesis(self, num_of_pairs: int) -> list[str]:
        all_combinations = []

        def combinations_search(left_count, right_count, prob_comb):
            if len(prob_comb) == num_of_pairs * 2:
                all_combinations.append(prob_comb)
                return
            if left_count < num_of_pairs:
                combinations_search(left_count + 1, right_count, prob_comb + "(")
            if right_count < left_count:
                combinations_search(left_count, right_count + 1, prob_comb + ")")

        combinations_search(0, 0, "")
        return all_combinations


check = Solution()
print(check.generateParenthesis(7))
