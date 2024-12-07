"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/binary-search-tree-iterator/description
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15, TreeNode(9), TreeNode(20))
iterator = BSTIterator(root)
print(iterator.next())
