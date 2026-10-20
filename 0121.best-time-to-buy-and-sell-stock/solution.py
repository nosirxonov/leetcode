# Created by Jonibek-Dev at 2026/10/20 14:06
# leetgo: 1.5.1
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_p = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_p:
                max_p = price - min_price
                
        return max_p

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
