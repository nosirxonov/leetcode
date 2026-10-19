# Created by Jonibek-Dev at 2026/10/19 12:22
# leetgo: 1.5.1
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().targetIndices(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
