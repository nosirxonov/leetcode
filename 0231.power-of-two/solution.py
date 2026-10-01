# Created by Jonibek-Dev at 2026/10/01 12:09
# leetgo: 1.4.18
# https://leetcode.com/problems/power-of-two/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isPowerOfTwo(n)
    print("\noutput:", serialize(ans, "boolean"))
