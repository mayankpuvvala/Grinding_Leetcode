class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low , high = max(weights), sum(weights)
        result = 0
        while low< high:
            k= (low+high)//2
            sumi, days_needed = 0, 1
            for i in weights:
                if (sumi+i) > k:
                    sumi = 0 
                    days_needed += 1
                sumi += i
            if days_needed <= days:
                high = k
            else:
                low = k+1
        return low


