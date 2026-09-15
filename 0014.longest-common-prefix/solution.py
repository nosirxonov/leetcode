# Created by Jonibek-Dev at 2026/09/15 13:43
# leetgo: 1.4.18
# https://leetcode.com/problems/longest-common-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
    
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestCommonPrefix(strs)
    print("\noutput:", serialize(ans, "string"))
