class Solution:
    def tribonacci(self, n: int) -> int:
        one, two, three= 0, 1, 1
        if n<3:
            return 0 if n==0 else 1
        for _ in range(n-2):
            three, two, one= three+two+one, three, two
        return three