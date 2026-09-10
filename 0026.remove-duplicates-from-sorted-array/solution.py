# Created by Jonibek-Dev at 2026/09/10 10:41
# leetgo: 1.4.18
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
                
        return k 

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().removeDuplicates(nums)
    print("\noutput:", serialize(ans, "integer"))
