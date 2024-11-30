"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/frequency-of-the-most-frequent-element/description
"""


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        current_cost = 0
        max_freq = 0
        for right in range(len(nums)):
            if right > 0:
                current_cost += (nums[right] - nums[right - 1]) * (right - left)
            while current_cost > k:
                current_cost -= nums[right] - nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)

        return max_freq


answer = Solution()
print(answer.maxFrequency([1, 2, 4], 5))
print(answer.maxFrequency([1, 4, 8, 13], 5))
print(answer.maxFrequency([3, 9, 6], 2))
