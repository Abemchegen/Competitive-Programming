class Bitset:

    def __init__(self, size: int):
        self.size=size
        self.li=[0]*size 
        self.re=[1]*size
        self.ones=0
        

    def fix(self, idx: int) -> None:
        if self.li[idx]==0:
            self.li[idx]=1
            self.re[idx]=0
            self.ones+=1
        

    def unfix(self, idx: int) -> None:
        if self.li[idx]==1:
            self.li[idx]=0
            self.re[idx]=1
            self.ones-=1
        

    def flip(self) -> None:
        self.ones=self.size-self.ones
        self.li,self.re=self.re,self.li
        

    def all(self) -> bool:
        if self.ones==self.size:
            return True
        else:
            return False
        

    def one(self) -> bool:
        if self.ones!=0:
            return True 
        else:
            return False
        

    def count(self) -> int:
        return self.ones
        

    def toString(self) -> str:
        ans=""

        for i in self.li:
            ans+=str(i)
        return ans
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()