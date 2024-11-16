"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/maximum-erasure-value/description
"""


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        set_nums = []
        summ_set = 0
        score = 0
        i = 0
        while i < len(nums):
            if nums[i] in set_nums:
                item_index = set_nums.index(nums[i])
                summ_set -= sum(set_nums[:item_index])
                set_nums = set_nums[item_index + 1 :]
                set_nums.append(nums[i])
            else:
                set_nums.append(nums[i])
                summ_set += nums[i]
            score = max(score, summ_set)
            i += 1
        return score


answer = Solution()
print(answer.maximumUniqueSubarray([4, 2, 4, 5, 6]))
print(answer.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
