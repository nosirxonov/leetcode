# 169. Majority Element

- **Manba:** https://leetcode.com/problems/majority-element/
- **Qiyinlik:** Easy
- **Tagiplar:** Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm
- **Metod:** `Solution.majorityElement(self, nums: list[int]) -> int`

## O'zbekcha tarjima

### Masala sharti
n o'lchamli massivni hisobga olgan holda, ko'pchilik elementni qaytaring. Koʻpchilik elementi ⌊n / 2⌋ martadan koʻproq koʻrinadigan elementdir. Ko'pchilik element har doim massivda mavjud deb taxmin qilishingiz mumkin.

### Cheklovlar (Constraints)
- n == sonlar.uzunlik

- 1 <= n <= 5 * 10^4

- -10^9 <= nums[i] <= 10^9

- Kirish shunday yaratiladiki, massivda ko'pchilik element mavjud bo'ladi.

### Qo'shimcha (Follow-up)
Muammoni chiziqli vaqt va fazoda hal qila olasizmi?

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
nums = [3,2,3]
```
**Output:**
```text
3
```

### Test 2
**Input:**
```text
nums = [2,2,1,1,1,2,2]
```
**Output:**
```text
2
```
