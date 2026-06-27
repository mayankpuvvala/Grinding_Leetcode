class Solution:
    def compress(self, chars: List[str]) -> int:
        i,write=0,0
        res= ""
        while i<len(chars):
            temp = chars[i]
            count= 0
            while i<len(chars) and chars[i]==temp:
                count+=1
                i+=1
            chars[write]= temp
            write+=1
            if count>1:
                for digit in str(count): 
                    chars[write]= digit
                    write+=1
            
        return write