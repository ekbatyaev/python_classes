"""
leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/random-flip-matrix/description
"""

from random import randint


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.matrix = set()

    def flip(self) -> list[int]:
        i, j = randint(0, self.m - 1), randint(0, self.n - 1)
        while (i, j) in self.matrix:
            i, j = randint(0, self.m - 1), randint(0, self.n - 1)
        self.matrix.add((i, j))
        return [i, j]

    def reset(self) -> None:
        self.matrix.clear()


answer = Solution(3, 3)
answer.flip()
