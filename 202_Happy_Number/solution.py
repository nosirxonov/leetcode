# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : 202. Happy Number
# Masala havolasi: https://leetcode.com/problems/happy-number/description/
# Platforma      : LeetCode (Easy)
# Metod          : Solution.isHappy(self, n: int) -> bool
# Tagiplar        : Hash Table, Math, Two Pointers, Floyd's Cycle Finding Algorithm
# Namuna testlar  : tests/ papkasida (python ../cf.py test)
# ====================================================================

class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = [4, 16, 37, 58, 89, 145, 42, 20]

        while n != 1 and n not in cycle:
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1
