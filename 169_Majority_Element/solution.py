# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : 169. Majority Element
# Masala havolasi: https://leetcode.com/problems/majority-element/
# Platforma      : LeetCode (Easy)
# Metod          : Solution.majorityElement(self, nums: list[int]) -> int
# Tagiplar        : Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm
# Namuna testlar  : tests/ papkasida (python ../cf.py test)
# ====================================================================

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        x = None
        count = 0

        for i in nums:
            if count == 0:
                x = i
            if i == x:
                count += 1
            else:
                count -= 1
        return x
