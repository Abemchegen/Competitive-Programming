class FrequencyTracker:

    def __init__(self):
        self.d=defaultdict(int)
        self.freq=defaultdict(int)


    def add(self, number: int) -> None:
        self.d[number]+=1
        self.freq[self.d[number]]+=1
        if self.freq[self.d[number]-1]:
            self.freq[self.d[number]-1]-=1

    def deleteOne(self, number: int) -> None:
        if self.d[number]:
            self.d[number]-=1
            if self.d[number]<=0:
                del self.d[number]
    
            self.freq[self.d[number]]+=1
            if self.freq[self.d[number]+1]:
                self.freq[self.d[number]+1]-=1

    def hasFrequency(self, frequency: int) -> bool:
        print(self.freq)
        if self.freq[frequency]:
            return True
        return False
        
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)