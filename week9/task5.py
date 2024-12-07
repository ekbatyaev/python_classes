"""
leetcode.com/problem-list/binary-tree/
url:https://leetcode.com/problems/path-sum-ii/description
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, current_path, current_sum):
            if not node:
                return

            current_path.append(node.val)
            current_sum += node.val

            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))

            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            current_path.pop()

        dfs(root, [], 0)
        return result


root = TreeNode(5)
root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root.right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
answer = Solution()
print(answer.pathSum(root, 22))