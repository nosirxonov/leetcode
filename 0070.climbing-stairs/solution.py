# Created by Jonibek-Dev at 2026/09/21 14:40
# leetgo: 1.4.18
# https://leetcode.com/problems/climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        prev2, prev1 = 1, 2
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)
    print("\noutput:", serialize(ans, "integer"))
