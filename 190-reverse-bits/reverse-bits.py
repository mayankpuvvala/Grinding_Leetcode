class Solution:
    def reverseBits(self, n: int) -> int:
        newt = int(bin(n)[2:].zfill(32)[::-1], 2)
        return newt