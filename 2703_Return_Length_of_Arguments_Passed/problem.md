# 2703. Return Length of Arguments Passed

- **Manba:** https://leetcode.com/problems/return-length-of-arguments-passed/
- **Qiyinlik:** Easy
- **Metod:** `Solution.argumentsLength(self, args) -> integer`

## O'zbekcha tarjima

### Masala sharti
Unga berilgan argumentlar sonini qaytaruvchi funksiya yozing.

### Cheklovlar (Constraints)
- args haqiqiy JSON massividir

- 0 <= args.length <= 100

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
args = [5]
```
**Output:**
```text
1
```
**Tushuntirish (Explanation):**
argumentsLength(5); // 1 Funktsiyaga bitta qiymat uzatildi, shuning uchun u 1 ni qaytarishi kerak.

### Test 2
**Input:**
```text
args = [{}, null, "3"]
```
**Output:**
```text
3
```
**Tushuntirish (Explanation):**
argumentsLength({}, null, "3"); // 3 Funktsiyaga uchta qiymat uzatildi, shuning uchun u 3 ni qaytarishi kerak.
