"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/fruit-into-baskets/description
"""


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        max_fruit = 0
        fruit_count = {}

        for right in range(len(fruits)):
            if fruits[right] in fruit_count:
                fruit_count[fruits[right]] += 1
            else:
                fruit_count[fruits[right]] = 1
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            max_fruit = max(max_fruit, right - left + 1)

        return max_fruit


answer = Solution()
print(answer.totalFruit([1, 2, 1]))
print(answer.totalFruit([0, 1, 2, 1]))
print(answer.totalFruit([1, 2, 3, 2, 2]))
