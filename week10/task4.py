"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/deepest-leaves-sum/description
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        deepest_sum = 0
        while queue:
            current_level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            deepest_sum = current_level_sum
        return deepest_sum


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5))
root.right = TreeNode(3)
root.right.right = TreeNode(6, None, TreeNode(8))

answer = Solution()
print(answer.deepestLeavesSum(root))
