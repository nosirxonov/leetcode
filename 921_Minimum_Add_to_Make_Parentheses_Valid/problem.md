# 921. Minimum Add to Make Parentheses Valid

- **Manba:** https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question
- **Qiyinlik:** Medium
- **Tagiplar:** String, Stack, Greedy, Bracket Sequences
- **Metod:** `Solution.minAddToMakeValid(self, s: str) -> int`

## O'zbekcha tarjima

### Masala sharti
Qavslar qatori quyidagi hollardagina amal qiladi:

- Bu bo'sh satr,

- U AB (B bilan birlashtirilgan A) sifatida yozilishi mumkin, bu erda A va B to'g'ri satrlar yoki

- U (A) shaklida yozilishi mumkin, bu erda A haqiqiy qatordir.

Sizga qavslar qatori berilgan s . Bitta harakatda siz satrning istalgan joyiga qavs qo'yishingiz mumkin.

- Misol uchun, agar s = "()))" bo'lsa, siz ochuvchi qavsni "( ( )))" yoki yopish qavsni "()) ) )" qilib qo'yishingiz mumkin.

s to'g'ri qilish uchun zarur bo'lgan harakatlarning minimal sonini qaytaring.

### Cheklovlar (Constraints)
- 1 <= s.uzunligi <= 1000

- s[i] '(' yoki ')' dir.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
s = "())"
```
**Output:**
```text
1
```

### Test 2
**Input:**
```text
s = "((("
```
**Output:**
```text
3
```
