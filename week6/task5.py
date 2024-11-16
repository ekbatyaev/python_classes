"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/minimum-size-subarray-sum/description
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        summ_arr = 0
        left = 0
        min_len = float("inf")
        for right in range(len(nums)):
            summ_arr += nums[right]
            if summ_arr >= target:
                while summ_arr >= target:
                    min_len = min(right - left + 1, min_len)
                    summ_arr -= nums[left]
                    left += 1
        if min_len == float("inf"):
            return 0
        return min_len


answer = Solution()
print(answer.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(answer.minSubArrayLen(4, [1, 4, 4]))
print(answer.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(answer.minSubArrayLen(11, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
