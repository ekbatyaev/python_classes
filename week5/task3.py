"""
leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/find-all-duplicates-in-an-array/description
"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        begin_len = len(nums)
        for i in range(len(nums)):
            if nums[i] in seen:
                nums.append(nums[i])
            else:
                seen.add(nums[i])
        return nums[begin_len:]


answer = Solution()
print(answer.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
