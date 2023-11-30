class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while(n>0):
            if n%3!=0 and (n-1 )% 3!=0 :
                return False
            n=n//3
            print(n)
        
        
        return True
        