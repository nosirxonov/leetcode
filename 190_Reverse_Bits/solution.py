# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : 190. Reverse Bits
# Masala havolasi: https://leetcode.com/problems/reverse-bits/description/
# Platforma      : LeetCode (Easy)
# Metod          : Solution.reverseBits(self, n: int) -> int
# Tagiplar        : Divide and Conquer, Bit Manipulation
# Namuna testlar  : tests/ papkasida (python ../cf.py test)
# ====================================================================

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
    
        if result >= 2**31:
            result -= 2**32
        
        return result
