# Created by Jonibek-Dev at 2026/09/12 08:27
# leetgo: 1.4.18
# https://leetcode.com/problems/remove-element/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
                
        return len(nums)

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    val: int = deserialize("int", read_line())
    ans = Solution().removeElement(nums, val)
    print("\noutput:", serialize(ans, "integer"))
