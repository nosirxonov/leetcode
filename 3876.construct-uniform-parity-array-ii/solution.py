# Created by Jonibek-Dev at 2026/09/03 13:03
# leetgo: 1.4.18
# https://leetcode.com/problems/construct-uniform-parity-array-ii/

import re
from typing import *
from leetgo_py import *

# @lc code=begin

# juft - juft = juft
# toq - toq = juft
# juft - toq = toq
# toq - juft = toq

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini = min(nums1)
        result = True
        if mini % 2 == 0:
            for i in nums1:
                if i % 2 != 0:
                    return False
                else:
                    result = True
        else:
            return True

        return result

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    ans = Solution().uniformArray(nums1)
    print("\noutput:", serialize(ans, "boolean"))
