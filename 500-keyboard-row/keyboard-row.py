class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiopQWERTYUIOP"
        second_row = "asdfghjklASDFGHJKL"
        third_row = "zxcvbnmZXCVBNM"
        result = []
        for string in words:
            check_in_row=0
            if string[0] in first_row:
                check_in_row= first_row
            elif string[0] in second_row:
                check_in_row= second_row
            else:
                check_in_row= third_row
            condition= False
            for i in string:
                if i.lower() not in check_in_row:
                    condition= True
                    break
            if condition== False:
                result.append(string)
        return result


