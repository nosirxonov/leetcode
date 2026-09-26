# Created by Jonibek-Dev at 2026/09/26 09:09
# leetgo: 1.4.18
# https://leetcode.com/problems/same-tree/

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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def func(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return func(p.left, q.left) and func(p.right, q.right)
        return func(p, q)
                

# @lc code=end

if __name__ == "__main__":
    p: TreeNode = deserialize("TreeNode", read_line())
    q: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSameTree(p, q)
    print("\noutput:", serialize(ans, "boolean"))
