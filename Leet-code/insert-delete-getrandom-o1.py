class RandomizedSet:

    def __init__(self):
        self.d={}
        self.li=[]
        self.index={}
        

    def insert(self, val: int) -> bool:
        if val in self.d :
            return False
        else:
            self.d[val]=1
            self.li.append(val)
            self.index[val]=len(self.li)-1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.d:
            
            self.li[self.index[val]], self.li[-1] = self.li[-1] , self.li[self.index[val]]
            self.index[self.li[self.index[val]]]= self.index[val]
            del self.index[val]
            del self.d[val]
            self.li.pop()
            
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        randomkey=random.choice(self.li)
        return randomkey
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()