# Created by Jonibek-Dev at 2026/09/01 08:38
# leetgo: 1.4.18
# https://leetcode.com/problems/roman-to-integer/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i < len(s) - 1 and sym[s[i]] < sym[s[i + 1]]:
                result -= sym[s[i]]
            else:
                result += sym[s[i]]
        
        return result

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().romanToInt(s)
    print("\noutput:", serialize(ans, "integer"))
