# Created by Jonibek-Dev at 2026/09/11 16:07
# leetgo: 1.4.18
# https://leetcode.com/problems/unique-3-digit-even-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digits_count = [0] * 10
        for d in digits:
            digits_count[d] += 1
            
        count = 0
        
        for h in range(1, 10):
            for t in range(10):
                for o in range(0, 10, 2):
                
                    required = [0] * 10
                    required[h] += 1
                    required[t] += 1
                    required[o] += 1
                
                    if (digits_count[h] >= required[h] and 
                        digits_count[t] >= required[t] and 
                        digits_count[o] >= required[o]):
                        count += 1
                    
        return count

# @lc code=end

if __name__ == "__main__":
    digits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().totalNumbers(digits)
    print("\noutput:", serialize(ans, "integer"))
