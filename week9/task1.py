"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/validate-binary-search-tree/description
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, lower, upper):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not validate(node.left, lower, val):
                return False
            if not validate(node.right, val, upper):
                return False

            return True

        return validate(root, float("-inf"), float("inf"))


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
answer = Solution()
print(answer.isValidBST(root))
