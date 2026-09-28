# Created by Jonibek-Dev at 2026/09/28 15:46
# leetgo: 1.4.18
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxDepth(self, s: str) -> int:
        x_list = []
        x = 0
        for i in s:
            if i == "(":
                x += 1
            elif i == ")":
                x_list.append(x)
                x -= 1
        return max(x_list) if x_list else 0

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maxDepth(s)
    print("\noutput:", serialize(ans, "integer"))
