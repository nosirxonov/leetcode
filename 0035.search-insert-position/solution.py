# Created by Jonibek-Dev at 2026/09/16 08:49
# leetgo: 1.4.18
# https://leetcode.com/problems/search-insert-position/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] < target:
                continue
            elif nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return i + 1

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchInsert(nums, target)
    print("\noutput:", serialize(ans, "integer"))
