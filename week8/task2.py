"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description
"""


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        if target < 0:
            return -1
        current_sum = 0
        left = 0
        max_length = -1
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_length = max(max_length, right - left + 1)
        if max_length == -1:
            return -1
        return len(nums) - max_length


answer = Solution()
print(answer.minOperations([1, 1, 4, 2, 3], 5))
print(answer.minOperations([5, 6, 7, 8, 9], 4))
print(answer.minOperations([3, 2, 20, 1, 1, 3], 10))
print(answer.minOperations([1, 1], 3))
