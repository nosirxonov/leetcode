# Created by Jonibek-Dev at 2026/08/31 15:10
# leetgo: 1.4.18
# https://leetcode.com/problems/palindrome-number/

from typing import *
import warnings
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().isPalindrome(x)
    print("\noutput:", serialize(ans, "boolean"))
