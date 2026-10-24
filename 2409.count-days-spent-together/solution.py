# Created by Jonibek-Dev at 2026/10/24 18:05
# leetgo: 1.5.1
# https://leetcode.com/problems/count-days-spent-together/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        startA = int(arriveAlice[3:]) + sum(months[:int(arriveAlice[:2]) - 1])
        startB = int(arriveBob[3:]) + sum(months[:int(arriveBob[:2]) - 1])
        endA = int(leaveAlice[3:]) + sum(months[:int(leaveAlice[:2]) - 1])
        endB = int(leaveBob[3:]) + sum(months[:int(leaveBob[:2]) - 1])
        start = max(startA, startB)
        end = min(endA, endB)
        if start <= end:
            return end - start + 1
        else:
            return 0

# @lc code=end

if __name__ == "__main__":
    arriveAlice: str = deserialize("str", read_line())
    leaveAlice: str = deserialize("str", read_line())
    arriveBob: str = deserialize("str", read_line())
    leaveBob: str = deserialize("str", read_line())
    ans = Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
    print("\noutput:", serialize(ans, "integer"))
