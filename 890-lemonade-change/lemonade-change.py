class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        newt= []
        for i in bills:
            if i==10:
                if 5 in newt:
                    newt.remove(5)
                    newt.append(10)
                else:
                    return False
            elif i==20:
                if 10 in newt:
                    newt.remove(10)
                    if 5 in newt:
                        newt.remove(5)
                    else:
                        return False
                elif 5 in newt:
                    newt.remove(5)
                    if 5 in newt:
                        newt.remove(5)
                        if 5 in newt:
                            newt.remove(5)
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
                newt.append(20)
                
            else:
                newt.append(5)
        return True