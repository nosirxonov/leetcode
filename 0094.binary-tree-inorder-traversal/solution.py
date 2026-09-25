# Created by Jonibek-Dev at 2026/09/25 09:11
# leetgo: 1.4.18
# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        nodes = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            nodes.append(node.val)
            traverse(node.right)
        traverse(root)
        return nodes


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().inorderTraversal(root)
    print("\noutput:", serialize(ans, "integer[]"))
