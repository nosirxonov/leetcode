# 258. Add Digits

- **Manba:** https://leetcode.com/problems/add-digits/description/
- **Qiyinlik:** Easy
- **Tagiplar:** Math, Simulation, Number Theory
- **Metod:** `Solution.addDigits(self, num: int) -> int`

## O'zbekcha tarjima

### Masala sharti
Agar butun son berilgan bo'lsa, natijada faqat bitta raqam bo'lguncha uning barcha raqamlarini qayta-qayta qo'shing va uni qaytaring.

### Cheklovlar (Constraints)
- 0 <= son <= 2^31 - 1

Kuzatish: O (1) ish vaqtida hech qanday tsikl/rekursiyasiz buni qila olasizmi?

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
num = 38
```
**Output:**
```text
2
```
**Tushuntirish (Explanation):**
Jarayon 38 --> 3 + 8 --> 11 11 --> 1 + 1 --> 2 2 faqat bitta raqamga ega bo'lgani uchun uni qaytaring.

### Test 2
**Input:**
```text
num = 0
```
**Output:**
```text
0
```
