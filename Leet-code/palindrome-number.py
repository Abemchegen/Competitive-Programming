class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        temp=0
        if x<0:
            return False
        while x>0:
         temp= temp *10 + x % 10
         x//= 10
        if y==temp: 
            return True
        else:
            return False 
     
    
        