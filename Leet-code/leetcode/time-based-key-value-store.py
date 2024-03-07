class TimeMap:

    def __init__(self):

        self.d = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        left = 0
        right = len(self.d[key]) - 1
        
        while left <= right:

            mid = (right + left) // 2

            if self.d[key][mid][0] <= timestamp:

                left = mid + 1

            else:
                right = mid - 1   

        if right == -1:
           return ""

        return self.d[key][right][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)