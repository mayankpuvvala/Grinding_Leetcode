class MyHashMap:

    def __init__(self):
        self.newt= [-5]*(10**6+1)

    def put(self, key: int, value: int) -> None:
        self.newt[key] = value


    def get(self, key: int) -> int:
        return self.newt[key] if self.newt[key]!=-5 else -1

    def remove(self, key: int) -> None:
        self.newt[key] = -5


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)