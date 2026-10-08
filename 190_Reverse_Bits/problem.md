# 190. Reverse Bits

- **Manba:** https://leetcode.com/problems/reverse-bits/description/
- **Qiyinlik:** Easy
- **Tagiplar:** Divide and Conquer, Bit Manipulation
- **Metod:** `Solution.reverseBits(self, n: int) -> int`

## O'zbekcha tarjima

### Masala sharti
Berilgan 32 bitli tamsayıning teskari bitlari. Kirish: n = 43261596 Chiqish: 964176192 Izoh: Butun ikkilik 43261596 00000010100101000001111010011100 964176192 00111001011110000010100101000000 Kirish: n = 2147483644 Chiqish: 1073741822 Izoh: Butun ikkilik 2147483644 011111111111111111111111 1073741822 0011111111111111111111111111110

### Cheklovlar (Constraints)
- 0 <= n <= 2^31 - 2

- n juft.

Kuzatish: Agar bu funksiya ko'p marta chaqirilsa, uni qanday optimallashtirasiz?

## Namunaviy testlar (Sample Tests)
