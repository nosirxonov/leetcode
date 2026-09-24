# Created by Jonibek-Dev at 2026/09/24 19:51
# leetgo: 1.4.18
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

from typing import *
from leetgo_py import *

# @lc code=begin

# Yana bir yechim

# for i, num in enumerate(nums):
#             if sum(int(digit) for digit in str(num)) == i:
#                 return i
#         return -1

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = 0
            temp = nums[i]
            while temp > 0:
                s += temp % 10
                temp //= 10
            if s == i:
                return i
        return -1

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallestIndex(nums)
    print("\noutput:", serialize(ans, "integer"))
