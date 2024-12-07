"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/recover-binary-search-tree/description
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)

        inorder(root)

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
answer = Solution()
answer.recoverTree(root)
