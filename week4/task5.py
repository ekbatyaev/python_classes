"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/spiral-matrix-ii/description/
"""


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        spiral = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        current_number = 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                spiral[top][i] = current_number
                current_number += 1
            top += 1

            for i in range(top, bottom + 1):
                spiral[i][right] = current_number
                current_number += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    spiral[bottom][i] = current_number
                    current_number += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    spiral[i][left] = current_number
                    current_number += 1
                left += 1

        return spiral


answer = Solution()
print(answer.generateMatrix(2))
