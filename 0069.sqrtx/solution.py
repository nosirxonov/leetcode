# Created by Jonibek-Dev at 2026/09/07 10:17
# leetgo: 1.4.18
# https://leetcode.com/problems/sqrtx/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
            
        left, right = 1, x
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().mySqrt(x)
    print("\noutput:", serialize(ans, "integer"))
