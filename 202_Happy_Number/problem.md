# 202. Happy Number

- **Manba:** https://leetcode.com/problems/happy-number/description/
- **Qiyinlik:** Easy
- **Tagiplar:** Hash Table, Math, Two Pointers, Floyd's Cycle Finding Algorithm
- **Metod:** `Solution.isHappy(self, n: int) -> bool`

## O'zbekcha tarjima

### Masala sharti
n soni baxtli yoki yo‘qligini aniqlash algoritmini yozing. Baxtli raqam - bu quyidagi jarayon orqali aniqlangan raqam:

- Har qanday musbat sondan boshlab, raqamni uning raqamlari kvadratlari yig'indisi bilan almashtiring.

- Raqam 1 ga teng bo'lguncha jarayonni takrorlang (u qaerda qoladi) yoki u 1 ni o'z ichiga olmaydi tsiklda cheksiz aylanadi.

- Ushbu jarayon 1 bilan tugaydigan raqamlar baxtlidir.

Agar n baxtli raqam bo'lsa true ni, bo'lmasa noto'g'ri qiymatini qaytaring.

### Cheklovlar (Constraints)
- 1 <= n <= 2^31 - 1

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
n = 19
```
**Output:**
```text
true
```
**Tushuntirish (Explanation):**
1^2 + 9^2 = 82 8^2 + 2^2 = 68 6^2 + 8^2 = 100 1^2 + 0^2 + 0^2 = 1

### Test 2
**Input:**
```text
n = 2
```
**Output:**
```text
false
```
