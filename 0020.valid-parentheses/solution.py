# Created by Jonibek-Dev at 2026/09/06 10:05
# leetgo: 1.4.18
# https://leetcode.com/problems/valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)
    print("\noutput:", serialize(ans, "boolean"))
