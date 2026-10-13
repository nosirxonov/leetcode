class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(nums, key=lambda x: x**2)
        score = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            score += nums[right] ** 2
            right -= 1
            if left <= right:
                score -= nums[left] ** 2
                left += 1
                
        return score   


# Juda sekin ammo to'g'ri)
