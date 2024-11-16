"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/arithmetic-slices/description
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        total_count = 0
        current_count = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current_count += 1
                total_count += current_count
            else:
                current_count = 0

        return total_count


answer = Solution()
print(answer.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]))
