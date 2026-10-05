# 856. Score of Parentheses

- **Manba:** https://leetcode.com/problems/score-of-parentheses/?envType=daily-question
- **Qiyinlik:** Medium
- **Tagiplar:** String, Stack, Bracket Sequences
- **Metod:** `Solution.scoreOfParentheses(self, s: str) -> int`

## O'zbekcha tarjima

### Masala sharti
muvozanatli qavslar mag'lubiyatga berilgan s, mag'lubiyatga ball qaytaring. Muvozanatlangan qavslar qatorining balli quyidagi qoidaga asoslanadi:

- "()" 1 ballga ega.

- AB A + B ballga ega, bu erda A va B tenglashtirilgan qavslar qatorlaridir.

- (A) 2 * A ballga ega, bu erda A muvozanatli qavslar qatoridir.

### Cheklovlar (Constraints)
- 2 <= s.uzunligi <= 50

- s faqat '(' va ')' dan iborat.

- s - muvozanatlangan qavslar qatori.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
s = "()"
```
**Output:**
```text
1
```

### Test 2
**Input:**
```text
s = "(())"
```
**Output:**
```text
2
```

### Test 3
**Input:**
```text
s = "()()"
```
**Output:**
```text
2
```
