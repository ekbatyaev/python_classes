"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/count-number-of-nice-subarrays/description
"""


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left = 0
        count = 0
        odd_count = 0
        for right in range(len(nums)):
            odd_count += nums[right] % 2
            while k < odd_count:
                odd_count -= nums[left] % 2
                left += 1
            if odd_count == k:
                temp_left = left
                while right >= temp_left and (nums[temp_left] % 2) == 0:
                    count += 1
                    temp_left += 1
                count += 1
        return count


answer = Solution()
print(answer.numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(answer.numberOfSubarrays([2, 4, 6], 1))
