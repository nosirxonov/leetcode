# 125. Valid Palindrome

- **Manba:** https://leetcode.com/problems/valid-palindrome/description/
- **Qiyinlik:** Easy
- **Tagiplar:** Two Pointers, String
- **Metod:** `Solution.isPalindrome(self, s: str) -> bool`

## O'zbekcha tarjima

### Masala sharti
Agar barcha bosh harflarni kichik harflarga aylantirib, alfanumerik bo'lmagan belgilarni olib tashlagandan so'ng, bir xil oldinga va orqaga o'qisa, ibora palindrom hisoblanadi. Alfanumerik belgilar harflar va raqamlarni o'z ichiga oladi. s satri berilgan bo'lsa , agar palindrom bo'lsa , true ni qaytaring , aks holda false ni qaytaring .

### Cheklovlar (Constraints)
- 1 <= s.uzunligi <= 2 * 10^5

- s faqat chop etiladigan ASCII belgilardan iborat.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
s = "A man, a plan, a canal: Panama"
```
**Output:**
```text
true
```
**Tushuntirish (Explanation):**
"amanaplanakanalpanama" - palindrom.

### Test 2
**Input:**
```text
s = "race a car"
```
**Output:**
```text
false
```
**Tushuntirish (Explanation):**
"poyga mashinasi" palindrom emas.

### Test 3
**Input:**
```text
s = " "
```
**Output:**
```text
true
```
**Tushuntirish (Explanation):**
s alfanumerik bo'lmagan belgilarni olib tashlaganidan keyin "" bo'sh qatordir. Bo'sh satr oldinga va orqaga bir xil o'qilgani uchun u palindromdir.
