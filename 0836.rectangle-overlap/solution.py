# Created by Jonibek-Dev at 2026/09/14 14:54
# leetgo: 1.4.18
# https://leetcode.com/problems/rectangle-overlap/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (rec1[0] < rec2[2] and 
                rec2[0] < rec1[2] and 
                rec1[1] < rec2[3] and 
                rec2[1] < rec1[3])
        
# @lc code=end

if __name__ == "__main__":
    rec1: List[int] = deserialize("List[int]", read_line())
    rec2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isRectangleOverlap(rec1, rec2)
    print("\noutput:", serialize(ans, "boolean"))
