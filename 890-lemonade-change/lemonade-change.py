class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0,0 
        for i in bills:
            if i==10:
                if not five:
                    return False
                five-=1
                ten+=1
            elif i==20:
                if ten:
                    ten-=1
                    if not five:
                        return False
                    five-=1
                elif five>2:
                    five-=3
                else:
                    return False
            else:
                five+=1
        return True