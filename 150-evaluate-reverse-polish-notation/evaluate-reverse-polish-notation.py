class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        newt='+-/*'
        self.stack=[]

        for tok in tokens:
            if tok in newt:
                b=int(self.stack.pop())
                a=int(self.stack.pop())
                if tok=="*":
                    self.stack.append(a*b)
                elif tok=="+":
                    self.stack.append(a+b)
                elif tok=="-":
                    self.stack.append(a-b)
                elif tok=="/":
                    self.stack.append(int(a/b))

            else:
                self.stack.append(int(tok))
        return self.stack[-1]