class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        present = set()
        
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq in present:
                res.add(seq)
            else:
                present.add(seq)
        return list(res)