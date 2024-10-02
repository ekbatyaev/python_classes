"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/permutations-ii/description/
"""

import itertools


class Solution:
    def permuteUnique(self, numbers: list[int]) -> list[list[int]]:
        return list(set(itertools.permutations(numbers)))


answer = Solution()
print(answer.permuteUnique([1, 1, 2]))
