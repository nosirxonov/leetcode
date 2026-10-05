# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : 258. Add Digits
# Masala havolasi: https://leetcode.com/problems/add-digits/description/
# Platforma      : LeetCode (Easy)
# Metod          : Solution.addDigits(self, num: int) -> int
# Tagiplar        : Math, Simulation, Number Theory
# Namuna testlar  : tests/ papkasida (python ../cf.py test)
# ====================================================================

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9
