class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        mult = 1
        if x < 0:
            mult = -1
            x = abs(x)
        while x > 0:
            digit = x % 10
            rev_num = rev_num * 10 + digit
            x //= 10
            # Check for overflow
            if rev_num > 2**31 - 1:
                return 0
        return rev_num * mult
