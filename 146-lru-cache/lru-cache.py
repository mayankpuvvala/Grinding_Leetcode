class LRUCache:

    def __init__(self, capacity: int):
        self.newt= {}
        self.capacity= capacity
        self.LRU= []

    def get(self, key: int) -> int:
        if key in self.newt:
            if key in self.LRU:
                self.LRU.remove(key)
            self.LRU.append(key)

            return self.newt[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.newt:
            self.newt[key]=value
        else:
            if len(self.newt)>=self.capacity:
                evict= self.LRU.pop(0)
                self.newt.pop(evict)
            self.newt[key]= value
        if key in self.LRU:
            self.LRU.remove(key)
        self.LRU.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)