class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict= set(wordDict)
        dp= [False]*(len(s)+1)
        dp[0]=True
        for i in range(len(s)):
            if dp[i]:
                for j in wordDict:
                    if s[i:i+len(j)]==j:
                        dp[i+len(j)]= True
        return dp[len(s)]
            