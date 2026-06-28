class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry= 0 
        i,j=len(a)-1, len(b)-1
        res=""
        while carry or i>-1 or j>-1:
            if i>-1:
                carry+=int(a[i])
                i-=1
            if j>-1:
                carry+=int(b[j])
                j-=1
            res+=str(carry%2)
            carry//=2
        return res[::-1]