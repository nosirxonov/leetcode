# Created by Jonibek-Dev at 2026/09/30 23:14
# leetgo: 1.4.18
# https://leetcode.com/problems/pascals-triangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [None] * (row_num + 1)
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

# @lc code=end

if __name__ == "__main__":
    numRows: int = deserialize("int", read_line())
    ans = Solution().generate(numRows)
    print("\noutput:", serialize(ans, "integer[][]"))
