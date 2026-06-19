class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        newt = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                newt[pattern].append(word)
        #till here i got solution on my own, with NC explanation, below is bfs, should focus more on this, so i could do it next time. 
        visited= set([beginWord])
        q = deque([beginWord])
        res= 1
        while q:
            for i in range(len(q)):
                word= q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neighbor in newt[pattern]:
                        if neighbor in visited:
                            continue
                        visited.add(neighbor)
                        q.append(neighbor)
            res+=1
        return 0
