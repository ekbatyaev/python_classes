"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/binary-subarrays-with-sum/description
"""


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr) - 1
        while right - left >= k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        return arr[left : left + k]


answer = Solution()
print(answer.findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(answer.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1))
