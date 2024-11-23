"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/subarray-product-less-than-k/description
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        count = 0
        product_of_group = 1
        for right in range(len(nums)):
            product_of_group *= nums[right]
            while k <= product_of_group:
                product_of_group /= nums[left]
                left += 1
                if product_of_group == 1:
                    break
            count += right - left + 1
        return count


answer = Solution()
print(answer.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(answer.numSubarrayProductLessThanK([1, 2, 3], 0))
