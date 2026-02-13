class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i]==0:
                prev = (i==0 or flowerbed[i-1]==0)
                next = (i==length -1 or flowerbed[i+1]==0)
                if prev and next:
                    print(i)
                    n-=1
                    flowerbed[i]= 1
            if n<=0:
                return True
        return False
