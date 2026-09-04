# Created by Jonibek-Dev at 2026/09/04 10:05
# leetgo: 1.4.18
# https://leetcode.com/problems/smallest-stable-index-i/

from typing import *
from leetgo_py import *

# @lc code=begin

# yechim uchun AI dan yordam olingan

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suff_min = [0] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < curr_min:
                curr_min = nums[i]
            suff_min[i] = curr_min
        
        curr_max = float('-inf')
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            
            if curr_max - suff_min[i] <= k:
                return i
                
        return -1

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().firstStableIndex(nums, k)
    print("\noutput:", serialize(ans, "integer"))
