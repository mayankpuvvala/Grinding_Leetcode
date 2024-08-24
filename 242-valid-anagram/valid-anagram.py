class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen= {}
        if len(s) != len(t):
            return False
        for num in s:
            seen[num]=seen.get(num,0)+1

        for num in t:
            seen[num]=seen.get(num,0)-1

        for num in seen:
            if seen[num] != 0:
                return False
        return True