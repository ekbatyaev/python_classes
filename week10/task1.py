"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/unique-binary-search-trees/description
"""


class Solution:
    def numTrees(self, n: int) -> int:
        nodes_num = [0] * (n + 1)
        nodes_num[0] = 1
        nodes_num[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                nodes_num[i] += nodes_num[j] * nodes_num[i - j - 1]
        return nodes_num[n]


answer = Solution()
print(answer.numTrees(3))
