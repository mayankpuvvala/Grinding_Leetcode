class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def dfs(num, n, k, res):
            if n==0:
                res.append(num)
                return
            lastdigit= num%10
            if (lastdigit+k<=9):
                dfs(num*10+lastdigit+k, n-1, k, res)
            if (k!=0 and lastdigit-k>=0):
                dfs(num*10+ lastdigit - k , n-1, k, res)
        for num in range(1,10):
            dfs(num, n-1, k, res)
        return res
