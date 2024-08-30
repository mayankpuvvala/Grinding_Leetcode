class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ''
        t_count= Counter(t)

        required= len(t_count)

        min_len= float('inf')
        min_window=''

        window_counts={}

        formed= 0

        left=right=0

        while  right<len(s):
            char = s[right]

            window_counts[char]=window_counts.get(char, 0)+1

            if char in t_count and t_count[char]==window_counts[char] :
                formed+=1
            
            while left<=right and formed == required:

                char = s[left]

                if right-left+1 < min_len:
                    min_len = right-left +1
                    min_window= s[left:right +1]
                
                window_counts[char]-=1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed-=1
                    
                left+=1
            right+=1
        return min_window

        