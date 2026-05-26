class MyHashMap:

    def __init__(self):
        self.size= 1000
        self.newt= [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        if self.newt[key%self.size]:
            for idx, (i,j) in enumerate(self.newt[key%self.size]):
                if i==key:
                    self.newt[key%self.size][idx]= [key, value]
                    return
                
        self.newt[key%self.size].append([key, value])

    def get(self, key: int) -> int:
        if self.newt[key%self.size]:
            for i,j in self.newt[key%self.size]:
                if i==key:
                    return j
        return -1

    def remove(self, key: int) -> None:
        for idx,(i,j) in enumerate(self.newt[key%self.size]):
            if i==key:
                self.newt[key%self.size].remove([i,j])
                print(self.newt[key%self.size])
                return
        return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)