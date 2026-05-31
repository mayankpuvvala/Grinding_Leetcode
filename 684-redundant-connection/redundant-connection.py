class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        t= [i for i in range(len(edges)+1)]
        
        for i,j in edges:
            if t[i]==t[j]:
                return [i,j]
            temp = t[i]
            for idx in range(len(t)):
                if t[idx]==temp:
                    t[idx]= t[j]
        return -1
        # uses the concept of using char's wrt indices, and this temp gets the original value instead of the updated value in the 2nd if