# Created by Jonibek-Dev at 2026/09/09 15:30
# leetgo: 1.4.18
# https://leetcode.com/problems/count-commas-in-range-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        k = 1
        while 10**(3 * k) <= n:
            total += (n - 10**(3 * k) + 1)
            k += 1
        return total

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countCommas(n)
    print("\noutput:", serialize(ans, "long"))
