# Created by Jonibek-Dev at 2026/09/08 16:09
# leetgo: 1.4.18
# https://leetcode.com/problems/count-commas-in-range/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countCommas(self, n: int) -> int:
        size = len(str(n))
        if size > 3:
            return (size // 4) * (n - 1000) + 1
        else:
            return 0

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countCommas(n)
    print("\noutput:", serialize(ans, "integer"))
