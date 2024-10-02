"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/jump-game-ii/description/
"""


class Solution:
    def jump(self, numbers: list[int]) -> int:
        min_steps = [0] * len(numbers)
        for i in range(len(numbers)):
            min_steps[i] = i
        for from_ind in range(len(numbers)):
            dest = 0
            while dest <= numbers[from_ind] and from_ind + dest < len(numbers):
                min_steps[from_ind + dest] = min(
                    min_steps[from_ind] + 1, min_steps[from_ind + dest]
                )
                dest += 1
        return min_steps[-1]


answer = Solution()
print(answer.jump([2, 3, 1, 1, 4]))
