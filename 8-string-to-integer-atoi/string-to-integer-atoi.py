class Solution:
    def myAtoi(self, s: str) -> int:
        num=""
        for i in s:
            if  (i>='0' and i<='9') :
                num+=i
            elif i==" ":
                if not num:
                    continue
                else:
                    break
            elif not num and i in "+-":
                num+=i
            else:
                break
        if not num or num in "+-":
            return 0
        if int(num)>=pow(2,31)-1:
            return  pow(2,31) -1
        elif int(num)<=pow(-2,31):
            return  pow(-2,31) 
        return int(num)  if num else 0