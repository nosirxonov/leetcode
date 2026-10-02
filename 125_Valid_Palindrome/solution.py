# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : 125. Valid Palindrome
# Masala havolasi: https://leetcode.com/problems/valid-palindrome/description/
# Platforma      : LeetCode (Easy)
# Metod          : Solution.isPalindrome(self, s: str) -> bool
# Tagiplar        : Two Pointers, String
# Namuna testlar  : tests/ papkasida (python ../cf.py test)
# ====================================================================

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        return s.lower() == s[::-1].lower()
