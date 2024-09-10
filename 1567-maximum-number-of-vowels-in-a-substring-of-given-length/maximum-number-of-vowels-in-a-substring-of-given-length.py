class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels= "aeiou"
        l,r= 0,0
        count=0
        maxi=0
        res=""
        while r<k:
            if s[r] in vowels:
                count+=1
                maxi= max(maxi,count)
            r+=1
                
        while r<len(s):
            if s[r] in vowels:
                count+=1
            r+=1
                
            if s[l] in vowels:
                count-=1
            l+=1
            maxi= max(maxi, count)
        return maxi

            
