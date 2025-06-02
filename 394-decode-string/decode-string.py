class Solution:
    def decodeString(self, s: str) -> str:
        stack= []
        for i in s:
            if i=="]":
                res= ""
                while stack[-1]!="[":
                    res=stack.pop()+res
                print(res)
                stack.pop()
                num= ""
                while stack and stack[-1]>="0" and stack[-1]<="9":
                    num = stack.pop()+num
                print(num)
                stack.append(res*int(num))
            else:
                stack.append(i)
        return "".join(stack)