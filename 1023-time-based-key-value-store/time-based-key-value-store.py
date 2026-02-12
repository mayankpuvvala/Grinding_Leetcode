class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.newt = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.newt[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.newt.get(key, [])
        fitting = bisect.bisect_right(values, (timestamp, chr(127)))
        return values[fitting - 1][1] if fitting> 0 else ""
               
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)