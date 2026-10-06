# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : 921. Minimum Add to Make Parentheses Valid
# Masala havolasi: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question
# Platforma      : LeetCode (Medium)
# Metod          : Solution.minAddToMakeValid(self, s: str) -> int
# Tagiplar        : String, Stack, Greedy, Bracket Sequences
# Namuna testlar  : tests/ papkasida (python ../cf.py test)
# ====================================================================

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        x = 0
        y = 0
        for i in s:
            if i == '(':
                x += 1
            elif x > 0 and i == ')':
                x -= 1
            else:
                y += 1
        return x + y
