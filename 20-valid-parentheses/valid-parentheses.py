class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i=0
        while i<len(s):
            while i<len(s) and  (s[i]=='('or s[i]=='{'or s[i]=='['):
                stack.append(s[i])
                i+=1
            if i<len(s) and stack and (s[i]==')' and stack[-1]!='(' or s[i]==']' and stack[-1]!='[' or s[i]=='}' and stack[-1]!='{'):        
                return False
            elif i<len(s):
                if stack:
                    stack.pop()
                else:
                    return False
            i+=1
        return not stack
