"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/3sum-closest/description/
"""


class Solution:
    def threeSumClosest(self, numbers: list[int], target: int) -> int:
        numbers.sort()
        n = len(numbers)
        # print(numbers)
        closest_sum = numbers[0] + numbers[1] + numbers[len(numbers) - 1]
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = numbers[i] + numbers[left] + numbers[right]

                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                if abs(closest_sum - target) > abs(current_sum - target):
                    closest_sum = current_sum
        return closest_sum


answer = Solution()
print(answer.threeSumClosest([-1, 2, 1, -4], 1))
print(answer.threeSumClosest([0, 1, 2], 3))
print(answer.threeSumClosest([1, 1, 1, 0], -100))
print(answer.threeSumClosest([2, 3, 8, 9, 10], 16))
