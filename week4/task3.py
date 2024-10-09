"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/sort-colors/description/
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        num_0 = nums.count(0)
        num_1 = nums.count(1)
        num_2 = nums.count(2)
        nums.clear()
        nums += [0] * num_0
        nums += [1] * num_1
        nums += [2] * num_2


answer = Solution()
print(answer.sortColors([2, 0, 2, 1, 1, 0]))
