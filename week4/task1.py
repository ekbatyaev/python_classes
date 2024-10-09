"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/triangle/description/
"""


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(
                    triangle[row + 1][col], triangle[row + 1][col + 1]
                )
        return triangle[0][0]


answer = Solution()

print(answer.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(answer.minimumTotal([[-1], [-2, -3]]))
