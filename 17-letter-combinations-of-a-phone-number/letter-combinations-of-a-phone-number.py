class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        newt= {"2":"abc", "3":"def",
                "4":"ghi","5":"jkl","6":"mno",
                "7":"pqrs","8":"tuv","9":"wxyz"}
        res= []
        def traversal(k, curStr):
            if len(curStr)==len(digits):
                res.append(curStr)
                return

            for i in (newt[digits[k]]):
                traversal(k+1, curStr+i)
        
        if digits:
            traversal(0,"")
        return res