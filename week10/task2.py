"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/binary-tree-level-order-traversal/description
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
answer = Solution()
print(answer.levelOrder(root))
