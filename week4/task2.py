"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/search-a-2d-matrix/description/
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        num_index = len(matrix)
        left = 0
        right = num_index
        while True:
            middle = (left + right) // 2
            if target == matrix[middle][0]:
                return True
            if right - left < 2:
                left_in = 0
                right_in = len(matrix[left])
                while True:
                    middle_in = (left_in + right_in) // 2
                    if right_in - left_in < 2:
                        return False
                    if target > matrix[left][middle_in]:
                        left_in = middle_in
                    elif target < matrix[left][middle_in]:
                        right_in = middle_in
                    elif target == matrix[left][middle_in]:
                        return True
            if target > matrix[middle][0]:
                left = middle
            elif target < matrix[middle][0]:
                right = middle


answer = Solution()
print(answer.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20],
                           [23, 30, 34, 60]], 13))
print(answer.searchMatrix([[1]], 1))
