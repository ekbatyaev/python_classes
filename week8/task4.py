"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description
"""


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        if k > len(arr):
            return 0
        window_summ = 0
        left = 0
        count = 0
        for right in range(len(arr)):
            window_summ += arr[right]
            if right - left + 1 == k:
                if (window_summ / k) >= threshold:
                    count += 1
                window_summ -= arr[left]
                left += 1
        return count


answer = Solution()
print(answer.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
