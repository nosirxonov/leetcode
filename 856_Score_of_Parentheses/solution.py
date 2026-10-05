# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : 856. Score of Parentheses
# Masala havolasi: https://leetcode.com/problems/score-of-parentheses/?envType=daily-question
# Platforma      : LeetCode (Medium)
# Metod          : Solution.scoreOfParentheses(self, s: str) -> int
# Tagiplar        : String, Stack, Bracket Sequences
# Namuna testlar  : tests/ papkasida (python ../cf.py test)
# ====================================================================

# Masala juda ham ajoyib)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        x = 1
        for i in range(len(s)):
            if s[i] == '(':
                x *= 2
            else:
                x //= 2

                if s[i - 1] == '(':
                    res += x
        return res
