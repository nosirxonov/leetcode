# Created by Jonibek-Dev at 2026/09/20 22:16
# leetgo: 1.4.18
# https://leetcode.com/problems/reverse-degree-of-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverseDegree(self, s: str) -> int:
        num = 0
        for i, char in enumerate(s, 1):
            index1 = ord(char) - ord('a') + 1
            index2 = 27 - index1
            num += index2 * i
    
        return num

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().reverseDegree(s)
    print("\noutput:", serialize(ans, "integer"))
