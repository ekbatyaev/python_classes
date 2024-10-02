"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/3sum/description/
"""


class Solution:
    def threeSum(self, numbers: list[int]) -> list[list[int]]:
        numbers.sort()
        all_combinations = []
        n = len(numbers)

        for i in range(n):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                current_sum = numbers[i] + numbers[left] + numbers[right]

                if current_sum == 0:
                    all_combinations.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1

                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return all_combinations


answer = Solution()
print(answer.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]))
