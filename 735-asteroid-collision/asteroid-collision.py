class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and stack[-1]>0 and i<0:
                if stack[-1]+i<0: stack.pop()
                elif stack[-1]+i>0: break
                else: stack.pop(); break
            else:
                stack.append(i)
        return stack