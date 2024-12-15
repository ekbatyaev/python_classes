"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/longest-univalue-path/description
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_path_length = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            left_univalue = (
                left_length + 1 if node.left and node.left.val == node.val else 0
            )
            right_univalue = (
                right_length + 1 if node.right and node.right.val == node.val else 0
            )
            self.max_path_length = max(
                self.max_path_length, left_univalue + right_univalue
            )
            return max(left_univalue, right_univalue)

        dfs(root)
        return self.max_path_length


root = TreeNode(5)
root.left = TreeNode(4, TreeNode(1), TreeNode(1))
root.right = TreeNode(5, TreeNode(5))

answer = Solution()
print(answer.longestUnivaluePath(root))
