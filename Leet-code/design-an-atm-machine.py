class ATM:

    def __init__(self):
        self.li=[0,0,0,0,0]
        self.copy=[0,0,0,0,0]
        self.d={0:20,1:50,2:100,3:200,4:500}
        self.ans=[]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(self.li)):
            self.li[i]+=banknotesCount[i]
     
        
    def withdraw(self, amount: int) -> List[int]:
        self.ans=[]
        self.copy=self.li[:]
        
        for i in range(len(self.copy)-1,-1,-1):
            
            if amount>0 and amount>= self.d[i] and self.copy[i]>0:

                got= min(amount//self.d[i], self.copy[i])
                self.ans.append(got)
                self.copy[i]-=got
                amount-=self.d[i] * got
            else:
                self.ans.append(0)
       
        if amount==0:
            self.ans.reverse()
            self.li=self.copy[:]
            return self.ans
        else:
            return [-1]
        
        

            
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)