class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if  "0000" in deadends:
            return -1
        visited= set(deadends)
        queue= deque()
        queue.append("0000")
        visited.add("0000")
        levels =0
        while queue:
            for _ in range(len(queue)):
                digit= queue.popleft()
                if digit == target:
                    return levels
                for i in range(4):
                    first= digit[:i]
                    num= int(digit[i])
                    second= digit[i+1:]
                    for change in [-1, 1]:
                        curr = (num+ change) %10
                        number= first+str(curr)+second
                        if number not in visited:
                            visited.add(number)
                            queue.append(number)
            levels+=1
        return -1