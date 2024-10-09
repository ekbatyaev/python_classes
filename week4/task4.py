"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        num_set = list(set(nums))
        value_data = []
        num_set.sort()
        for i in range(len(num_set)):
            count = nums.count(num_set[i])
            if count >= 2:
                value_data.append(2)
            else:
                value_data.append(count)
        nums.clear()
        for i in range(len(num_set)):
            nums += [num_set[i]] * value_data[i]
        print(nums)
        return len(nums)


answer = Solution()
print(answer.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(answer.removeDuplicates([-1, 0, 0, 0, 0, 3, 3]))
